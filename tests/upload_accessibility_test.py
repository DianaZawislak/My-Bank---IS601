""" Tests for access granted or denied to upload"""


def test_upload_denied(client):
    response = client.get("/browse_transactions", follow_redirects=False)
    assert response.status_code == 404


def test_upload_denied(client):
    response = client.get("/upload", follow_redirects=False)
    assert response.status_code == 404