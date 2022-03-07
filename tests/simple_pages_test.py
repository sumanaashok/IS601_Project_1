"""This tests all the webpages including index page"""

def test_request_main_menu_links(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/page1">GIT</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome To My Website" in response.data


def test_request_page1(client):
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"GIT" in response.data


def test_request_page2(client):
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Page 2" in response.data


def test_request_page3(client):
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Page 3" in response.data


def test_request_page4(client):
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Page 4" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404