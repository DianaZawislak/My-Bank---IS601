""" Dashboard accessibility tests"""


def test_dashboard_access_granted(client):
    response = client.post('/login', data={
        'email': 'diana@test,com',
        'password': 'diana123',
    }, follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/dashboard'
    html = response.get_data(as_text=True)
    assert '<p>Current Account Balance: {{ user_balance }} </p>' in html


def test_dashboard_access_denied(client):
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/login'
    html = response.get_data(as_text=True)
    assert 'Please log in to access this page.' in html
