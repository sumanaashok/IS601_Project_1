"""This tests all the webpages including index page"""


def test_request_main_menu_links(client):
    """
    This is a test for the main menu links
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/git">GIT</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/python-flask">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/ci-cd">CI/CD</a>' in response.data


def test_request_index(client):
    """This tests the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome To My Website" in response.data


def test_request_git_page(client):
    """This tests the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"GIT" in response.data


def test_request_docker_page(client):
    """This tests the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data


def test_request_python_flask(client):
    """This tests the python-flask page"""
    response = client.get("/python-flask")
    assert response.status_code == 200
    assert b"Python/Flask" in response.data


def test_request_ci_cd(client):
    """This tests the ci-cd page"""
    response = client.get("/ci-cd")
    assert response.status_code == 200
    assert b"CI/CD" in response.data


def test_request_page_not_found(client):
    """This tests a 404 page"""
    response = client.get("/page5")
    assert response.status_code == 404
