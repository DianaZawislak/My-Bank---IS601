""" Dashboard accessibility tests"""


def test_dashboard_acces_granted(client):
    response = client.get("/dashboard")
    assert response.status_code == 302



def test_dashboard_access_denied(client):
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/login'

