""" Testing registration, correct registration, with insufficient password,
    incorrect email format and mismatched passwords"""


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

def test_registeristration_email_wrong_format(client):
    #Testing registering with wrong email format
    response = client.post("/register", data={"email": "diana", "password": "aaaaa", "confirm": "aaaaa"})
    #there should be no redirection
    assert response.status_code == 200

def test_register_with_mismatched_passwords(client):
    #Testing registration fail when passwords dont match
    response = client.post("/register", data={"email": "diana@diana.com", "password": "aaaaaa", "confirm": "bbbbbb"},
                           follow_redirects=True)
    #no redirection should happen
    assert response.status_code == 200
    assert b"Passwords must match" in response.data