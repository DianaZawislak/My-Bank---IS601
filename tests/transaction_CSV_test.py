'''Testing CSV file '''
import os
import csv

from app import db
from app.db.models import User, Transaction
from app import create_app, db, config

BASE_DIR = config.Config.BASE_DIR
uploaddir = os.path.join(BASE_DIR, '../uploads')
test_file = os.path.join(uploaddir, 'test.csv')


def test_upload_dir():
    '''Tests for existence of upload directory'''
    if not os.path.exists(uploaddir):
        os.mkdir(uploaddir)
    assert os.path.exists(uploaddir)


def test_if_file_uploads(application, test_user):
    with application.app_context():
        assert db.session.query(User).count() == 1
        assert db.session.query(Transaction).count() == 0
    root = config.Config.BASE_DIR
    csv_file = 'transactions.csv'
    filepath = root + '/..app/uploads/' + csv_file
    uploadfolder = config.Config.UPLOAD_FOLDER
    file_upload = os.path.join(uploadfolder, csv_file)
    assert os.path.exists(file_upload) == True


def test_csv_processed(application, list_of_transactions=None):
    '''Tests processing of CSV'''
    # Creates db and test user to associate with transaction db
    with application.app_context():
        db.create_all()
        user = User('test@test.com', 'testtest')
        db.session.add(user)
        list_of_songs = []
        # CSV data is loaded to db
        with open(test_file) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_of_transactions.append(Transaction(row['AMOUNT'], row['TYPE']))
        user.transactions = list_of_songs
        db.session.commit()
        # Tests CSV data was successfully loaded to db
        test_transaction = Transaction.query.filter_by(id='1').first()
        assert test_transaction.id == '1'
        # Breaks down test user and confirms db is empty
        db.session.delete(user)
        assert db.session.query(User).count() == 0
    # Removes test csv
    os.remove(test_file)
    assert os.path.exists(test_file) == False