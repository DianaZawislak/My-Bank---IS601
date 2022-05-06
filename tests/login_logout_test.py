'''Testing of log in  and logout function'''



def test_login(client, application):
    response = client.post('/login', data={
        'email': 'diana@test.com',
        'password': 'testtest',
    }, follow_redirects=True)
    #if login succesfull user is redirected to index page(home)
    assert response.status_code == 200
    assert response.request.path == '/register'



def test_logout(client, application):
    """This tests the logout """
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/login'





