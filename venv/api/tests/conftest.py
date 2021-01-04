import pytest
from app import api_all

@pytest.fixture(scope="module")
def app():
    return api_all()