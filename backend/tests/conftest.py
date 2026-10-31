import os
os.environ['DATABASE_URL']='sqlite:///./test_agrimitra.db'; os.environ['SECRET_KEY']='test-secret-key-at-least-32-characters-long'
from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.db.base import Base
from app.db.session import engine
@pytest.fixture(autouse=True)
def clean_database():
 Base.metadata.drop_all(bind=engine); Base.metadata.create_all(bind=engine); yield; Base.metadata.drop_all(bind=engine)
@pytest.fixture
def client():
 with TestClient(app) as test_client: yield test_client
