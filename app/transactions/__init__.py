"""" Transactions blueprint"""

import csv
import logging
import os

from flask import Blueprint, render_template, abort, url_for, current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from sqlalchemy.engine import row
from sqlalchemy.sql.functions import user

from app.db import db, database
from app.db.models import Transaction
from app.logging_config import after_request_transactions_upload
from app.transactions.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

transactions = Blueprint('transactions', __name__,
                         template_folder='templates')


@transactions.route('/transactions', methods=['GET'], defaults={"page": 1})
@transactions.route('/transactions/<int:page>', methods=['GET'])
def transactions_browse(page):
    page = page
    per_page = 1000
    pagination = Transaction.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_transactions.html', data=data, pagination=pagination)
    except TemplateNotFound:
        abort(404)


@transactions.route('/transactions/upload', methods=['POST', 'GET'])
@login_required
def transactions_upload():
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("transactions_upload")
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        user = current_user
        list_of_transactions = []

        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_of_transactions.append(Transaction(row['Amount'], row['Type']))

        current_user.transactions += list_of_transactions
        db.session.commit()
        after_request_transactions_upload()
        current_app.logger.info(user.email + " has uploaded " + filename)
        return redirect(url_for('auth.dashboard'))

    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)


@transactions.route('/info/<id>')
def info(id):
    user_info = database.query.filter_by(id=id).first()
    return render_template('dashboard.html', information=user_info)


