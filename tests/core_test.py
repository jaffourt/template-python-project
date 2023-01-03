"""A simple unit test for the project's core functionality"""
import pytest

from my_package.core import make_request


@pytest.mark.parametrize("webpage, expected", [
    ("https://www.example.com", 200),
    ("https://www.google.com", 200),
])
def test_make_request(webpage, expected):
    """Tests the make_request functionality for various inputs"""
    response = make_request(webpage)
    assert expected == response.status_code
