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
        user = User('diana.zawislak@icloud.com', 'testtest', is_admin=1)
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        db.session.commit()
        #assert that we now have a new user
        assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='diana.zawislak@icloud.com').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'diana.zawislak@icloud.com'
        #this is how you get a related record ready for insert
        user.transactions= [Transaction(655.0,"DEBIT"),Transaction(480.0,"CREDIT")]
        #commit is what saves the transactions
        db.session.commit()
        assert db.session.query(Transaction).count() == 2
        transaction1 = Transaction.query.filter_by(type="DEBIT").first()
        assert transaction1.type == "DEBIT"
        #changing the type of the transaction
        transaction1.type = "CREDIT"
        #saving the new type of the transaction
        db.session.commit()
        transaction2 = Transaction.query.filter_by(type='CREDIT').first()
        assert transaction2.type == "CREDIT"
        #checking cascade delete
        db.session.delete(user)
        # assert db.session.query(User).count() == 0
        # assert db.session.query(Transaction).count() == 0