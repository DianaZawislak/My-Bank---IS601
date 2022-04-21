"""This is testing existence of log files individually"""

import os

root = os.path.dirname(os.path.abspath(__file__))
logdir = os.path.join(root, '../app/logs')


def test_errors_logfiles():
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/errors.log')
    assert os.path.exists(logfile) is True


def test_flask_logfiles():
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/flask.log')
    assert os.path.exists(logfile) is True


def test_myapp_logfiles():
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/myapp.log')
    assert os.path.exists(logfile) is True


def test_request_logfiles():
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/request.log')
    assert os.path.exists(logfile) is True


def test_sqlalchemy_logfiles():
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/sqlalchemy.log')
    assert os.path.exists(logfile) is True


def test_werkzeug_logfiles():
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/werkzeug.log')
    assert os.path.exists(logfile) is True


def test_debug_logfiles():
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/debug.log')
    assert os.path.exists(logfile) is True


def test_dianasapp_logfiles():
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/dianasapp.log')
    assert os.path.exists(logfile) is True
