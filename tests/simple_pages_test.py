"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/home")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data



def test_request_index(client):
    """This makes the index page"""
    response = client.get("/home")
    assert response.status_code == 200
    assert b"Easiest Banking." in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data

#def test_request_page1(client):
#   """This makes the index page"""
#  response = client.get("/welcome")
#   assert response.status_code == 200
#    assert b"welcome" in response.data


def test_request_dashboard(client):
    """This tests dashboard """
    # redirect to /login since not authenticated
    response = client.get("/dashboard", follow_redirects=True)
    assert response.status_code == 200
    assert b"If you do not have an account, please" in response.data


def test_request_login(client):
    """This tests the login """
    response = client.get("/login")
    assert response.status_code == 200
    assert b"If you do not have an account, please" in response.data


def test_request_registration(client):
    """ this tests /registration """
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register<" in response.data



def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404