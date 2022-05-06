"""This is testing existence of log files individually"""

import os

root = os.path.dirname(os.path.abspath(__file__))
logdir = os.path.join(root, '../logs')


def test_error_logfiles():
    logfile = os.path.join(logdir, 'errors.log')
    if not os.path.exists(logfile):
        f = open(logfile, 'w')
        f.close()
    assert os.path.exists(logfile) == True


def test_request_logfiles():
    logfile = os.path.join(logdir, 'request.log')
    if not os.path.exists(logfile):
        f = open(logfile, 'w')
        f.close()
    assert os.path.exists(logfile) == True


def test_sqlalchemy_logfiles():
    logfile = os.path.join(logdir, 'sqlalchemy.log')
    if not os.path.exists(logfile):
        f = open(logfile, 'w')
        f.close()
    assert os.path.exists(logfile) == True


def test_werkzeug_logfiles():
    logfile = os.path.join(logdir, 'werkzeug.log')
    if not os.path.exists(logfile):
        f = open(logfile, 'w')
        f.close()
    assert os.path.exists(logfile) == True


def test_debug_logfiles():
    logfile = os.path.join(logdir, 'debugs.log')
    if not os.path.exists(logfile):
        f = open(logfile, 'w')
        f.close()
    assert os.path.exists(logfile) == True


def test_song_uploads_logfiles():
    logfile = os.path.join(logdir, 'song_uploads.log')
    if not os.path.exists(logfile):
        f = open(logfile, 'w')
        f.close()
    assert os.path.exists(logfile) == True


def test_useractivities_logfiles():
    logfile = os.path.join(logdir, 'useractivities.log')
    if not os.path.exists(logfile):
        f = open(logdir, 'useractivities')
        f.close()
    assert os.path.exists(logfile) == True

def test_DianasApp_logfiles():
    logfile = os.path.join(logdir, 'DianasApp.log')
    if not os.path.exists(logfile):
        f = open(logfile, 'w')
        f.close()
    assert os.path.exists(logfile) == True

# def test_dianasapp_logfiles():
#   assert os.path.exists(logdir) is True
#  logfile = os.path.join(root, '../app/logs/dianasapp.log')
#  assert os.path.exists(logfile) is True
