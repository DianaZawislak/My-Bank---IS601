""" Testing registration"""


def test_registration(client, application):
    response = client.post('/register', data={
        'email': 'diana@test.com',
        'password': 'password',
        'confirm': 'password'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/register_login'

def test_registeristration_password_not_satisfied(client):
    #Testing registering with password not meeting requirements (min 6 characters)
    response = client.post("/register", data={"email": "diana@test.com", "password": "aaa", "confirm": "aaa"})
    #there should be no redirection
    assert response.status_code == 200