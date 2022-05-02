'''Testing of log in function'''

from werkzeug.security import generate_password_hash

from app import db
from app.db.models import User


user = User('diana@test.com', generate_password_hash('diana123'))
data = {'email': 'diana@test.com', 'password': 'diana123'}


def test_login(client, application):
    '''Tests login and auto navigation to dashboard'''
    #Test user injected into db - this persists through rest of the testing in this file
    with application.app_context():
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1
        response = client.post('/login', data=data, follow_redirects=True)
        assert response.status_code == 200
        #Successful log in routes to dashboard page
        assert b"Dashboard" in response.data

def test_logout(client, test_user):
    # pylint: disable=unused-argument,redefined-outer-name
        response = client.get('/logout')
        # go to index if logged in
        assert response.status_code == 302
        assert b'login' in response.data
        assert test_user.is_authenticated() == False





