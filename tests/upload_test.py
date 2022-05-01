""" Tests for access granted or denied to dashboard"""

from werkzeug.security import generate_password_hash
from app.db.models import User

user = User('diana@test.com', generate_password_hash('diana123'))
data = {'email': 'diana@test.com', 'password': 'diana123'}

def test_upload_denied(client):
    '''Tests that upload is not accessible when user not logged in '''
    response = client.get("/upload")
    assert response.status_code == 404


def test_upload_access_granted(client, application):
    '''Tests access to upload page when logged in'''
    @application.login_manager.request_loader
    def load_user_from_request(request):
        return User.query.first()
    response = client.get('/songs')
    assert response.status_code == 200
    assert b"Upload" in response.data

