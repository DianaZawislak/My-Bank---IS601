"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name
import logging
import os

import pytest
from flask.testing import FlaskClient
from flask_login import FlaskLoginClient

from app import create_app, User
from app.db import db

#this is a good tutorial I used to fix this code to do datbase testing.
#https://xvrdm.github.io/2017/07/03/testing-flask-sqlalchemy-database-with-pytest/

@pytest.fixture()
def application():
    """This makes the app"""
    #you need this one if you want to see whats in the database
    #os.environ['FLASK_ENV'] = 'development'
    #you need to run it in testing to pass on github
    os.environ['FLASK_ENV'] = 'testing'
    application = create_app()
    application.test_client_class = FlaskLoginClient
    application.config['WTF_CSRF_ENABLED'] = False

    application = create_app()

    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        #drops the database tables after the test runs
        #db.drop_all()


@pytest.fixture()
def add_user(application):
    with application.app_context():
        #new record
        user = User('test@test.com', 'testtest')
        db.session.add(user)
        db.session.commit()




@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()

@pytest.fixture()
def app_client(application):
    ctx = application.test_request_context()
    ctx.push()
    application.test_client_class = FlaskClient
    return application.test_client()

@pytest.fixture
def add_db_user_fixture(application):
    """ setup database user and delete """

    with application.app_context():
        assert db.session.query(User).count() == 0 # pylint: disable=no-member

        user_email = 'testuser@test.com'
        user_password = 'testtest'
        user = User(user_email, user_password)
        db.session.add(user) # pylint: disable=no-member

        user = User.query.filter_by(email=user_email).first()
        assert user.email == user_email
        db.session.commit() # pylint: disable=no-member

        yield user

        db.session.delete(user) # pylint: disable=no-member
        assert db.session.query(User).count() == 0 # pylint: disable=no-member
        assert db.session.query(Song).count() == 0 # pylint: disable=no-member