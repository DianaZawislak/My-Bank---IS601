"""This tests specific user balance calculation"""

from werkzeug.security import generate_password_hash

from app import User, db
from app.db.models import Transaction


def test_user_balance(application):
    """Tests the user balance"""
    # pylint: disable=no-member
    # Create user for the test case
    user = User('test@test.com', generate_password_hash('test1234'), is_admin=1)
    with application.app_context():
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1
        user.authenticated = True

        # Dummy transaction
        user.transactions = [Transaction(2000, "Credit 1"), Transaction(3000, "Credit 2")]
        db.session.commit()
        assert db.session.query(Transaction).count() == 2

        # Searching for transactions filtered by user id and sums them up
        userid = user.id
        user_trans = Transaction.query.filter_by(user_id=userid).all()
        total = 0
        for trans in user_trans:
            total += trans.amount
        assert total == 5000