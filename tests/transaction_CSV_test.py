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


def test_upload_csv():
    '''Tests for csv file creation/existence'''
    fields = ['AMOUNT', 'TYPE', 'BALANCE']
    rows = [['2000', 'DEBIT', '0']]

    with open(test_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    assert os.path.exists(test_file)


def test_csv_processed(application):
    '''Tests processing of CSV'''
    # Creates db and test user to associate w/ song db
    with application.app_context():
        db.create_all()
        user = User('test@test.com', 'testtest')
        db.session.add(user)
        list_of_songs = []
        # Loads CSV data to db
        with open(test_file) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list_of_songs.append(Transaction(row['AMOUNT'], row['TYPE'], row['BALANCE']))
        user.songs = list_of_songs
        db.session.commit()
        # Tests CSV data was successfully loaded to db
        test_song = Transaction.query.filter_by(title='California Love').first()
        assert test_song.title == 'California Love'
        # Breaks down test user and confirms db is empty
        db.session.delete(user)
        assert db.session.query(User).count() == 0
    # Removes test csv
    os.remove(test_file)
    assert os.path.exists(test_file) == False