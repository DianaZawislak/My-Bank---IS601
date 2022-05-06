""" Testing registration"""


def test_registration(client, application):
    response = client.post('/register', data={
        'email': 'diana@test.com',
        'password': 'password',
        'confirm': 'password'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/register_login'