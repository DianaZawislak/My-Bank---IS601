'''Testing of log in  and logout function'''

from werkzeug.security import generate_password_hash

from app import db
from app.db.models import User


def test_login(client, application):
    response = client.post('/login', data={
        'email': 'diana@test.com',
        'password': 'testtest',
    }, follow_redirects=True)
    #if login succesfull user is redirected to index page(home)
    assert response.status_code == 200
    assert response.request.path == '/index'
    html = response.get_data(as_text=True)
    assert '<p class="text-light pb-3"> Let us help you and your family become financially independent</p>' in html


def test_logout(client, application):
    """This tests the logout """
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"<h2>Login</h2>" in response.data





