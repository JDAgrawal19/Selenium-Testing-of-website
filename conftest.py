import pytest


# Command line options:
# Example of allowing pytest to accept a command line option
def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     default="chrome",
                     help="Browser. Valid options are firefox or chrome")


# Test arguments:
# Example of populating the argument 'browser' for a test
@pytest.fixture
def browser(request):
    "pytest fixture for browser"
    return request.config.getoption("-B")

