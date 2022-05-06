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


def test_if_file_uploads(application):
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
    root = config.Config.BASE_DIR
    csv_file = 'trans.csv'
    filepath = root + '/..app/uploads/' + csv_file
    uploadfolder = config.Config.UPLOAD_FOLDER
    file_upload = os.path.join(uploadfolder, csv_file)
    assert os.path.exists(file_upload) == True


#def test_csv_processed(application):
#    '''Tests processing of CSV'''
#    with application.app_context():
#        db.create_all()
#        user = User('test@test.com', 'testtest', is_admin=1)
#        db.session.add(user)
#        list_of_transactions = []
#        with open(test_file) as file:
#            csv_file = csv.DictReader(file)
#           for row in csv_file:
#                list_of_transactions.append(Transaction(row['amount'], row['type']))
#        user.transactions = list_of_transactions
#        db.session.commit()
#        test_song = Transaction.query.filter_by(type='CREDIT').first()
#        assert test_song.type == 'CREDIT'
#        db.session.delete(user)
#        assert db.session.query(User).count() == 0
#    os.remove(test_file)
#    assert os.path.exists(test_file) == False