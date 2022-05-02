import logging

from app import db
from app.db.models import User, Transaction
from faker import Faker

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        #showing how to add a record
        #create a record
        user = User('dog@dog.com', 'aaaaaa')
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        db.session.commit()
        #assert that we now have a new user
        assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='dog@dog.com').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'dog@dog.com'
        #this is how you get a related record ready for insert
        user.transactions = [Transaction("test", "smap", "dsf"), Transaction("test2", "te", "dsf")]
        db.session.commit()
        assert db.session.query(Transaction).count() == 2
        transaction1 = Transaction.query.filter_by(title='test').first()
        assert transaction1.title == "test"
        transaction1.title = "Supertransaction"
        db.session.commit()
        transaction2 = Transaction.query.filter_by(title='Supertransaction').first()
        assert transaction2.title == "Supertransaction"
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0