from werkzeug.security import generate_password_hash
from app.db.models import User

data = {'email': 'diana@test.com', 'password': 'diana123'}
user = User('diana@test.com', generate_password_hash('diana123'))

def test_dashboard_access_denied(client):
    '''Tests dashboard not accesible when not logged in'''
    response = client.get('/dashboard', follow_redirects=False)
    assert response.status_code == 302
    #Unauthenticated users are redirected to Login page'''
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data


#def test_dashboard_access_granted(client):
#    response = client.post('/login', data=data, follow_redirects=True)
 #   assert response.status_code == 200
    # Successful log in routes to dashboard page
  #  assert b"Dashboard" in response.data