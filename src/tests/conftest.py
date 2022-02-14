# src/tests/conftest.py


import pytest
import uuid

from config.secrets import get_secret
from src.api import create_app


@pytest.fixture(scope="module")
def test_app():
    app = create_app(get_secret())
    with app.app_context():
        yield app  # testing happens here
