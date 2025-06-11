import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env_test'))

import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.config import API_PREFIX

client = TestClient(app)

@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown_db():
    # Setup and teardown handled by conftest.py
    pass

# All tests remain the same as before, using the test client and API_PREFIX
from src.test_main import *
