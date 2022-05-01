import os

from flask import request
from werkzeug.security import generate_password_hash

from app import db
from app.db.models import User


user = User('test@test.com', generate_password_hash('aaaaaa'))
data = {'email': 'test@test.com', 'password': 'aaaaaa'}

def test_registration(client, application):
    '''Tests user registration'''
    #Test starts assuming there is no user in db
    assert db.session.query(User).count() == 0
    with application.app_context():
        response = client.post('/register', data=data, follow_redirects=True)
        assert response.status_code == 200
        #Successful registration auto routes to login page
        assert b"login" in response.data