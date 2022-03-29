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
    assert b'<a class="nav-link" href="/OOP">OOP-Glossary</a>' in response.data
    assert b'<a class="nav-link" href="/AAA-Testing">AAA-Testing</a>' in response.data
    assert b'<a class="nav-link" href="/calculator_OOP">OOP-Calculator</a>' in response.data


def test_request_index(client):
    """This tests the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome To My Website" in response.data


def test_request_git_page(client):
    """This tests the git page"""
    # The Arrange phase
    url_to_request = "/git"
    # Act Phase
    response = client.get(url_to_request)
    # The Assert Phase
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


def test_request_oop(client):
    """This tests the OOP page"""
    response = client.get("/OOP")
    assert response.status_code == 200
    assert b"OOP-Glossary" in response.data


def test_request_aaa(client):
    """This tests the AAA testing page"""
    response = client.get("/AAA-Testing")
    assert response.status_code == 200
    assert b"AAA-Testing" in response.data


def test_request_calculator_oop(client):
    """This tests the calculator_OOP page"""
    response = client.get("/calculator_OOP")
    assert response.status_code == 200
    assert b"OOP-Calculator" in response.data


def test_request_page_not_found(client):
    """This tests a 404 page"""
    response = client.get("/page5")
    assert response.status_code == 404
