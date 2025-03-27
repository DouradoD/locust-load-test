import pytest
from tests.api.user import app, db, User
import json


@pytest.fixture
def client():
    # Configure test database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create test tables
        yield client
        with app.app_context():
            db.drop_all()  # Cleanup after tests


def test_create_user(client):
    """Test user creation"""
    response = client.post('/users',
                           json={'name': 'Test User', 'email': 'test@example.com'})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'Test User'


def test_get_users(client):
    """Test retrieving all users"""
    # First create a test user
    client.post('/users',
                json={'name': 'Test User', 'email': 'test@example.com'})

    response = client.get('/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['email'] == 'test@example.com'


def test_update_user(client):
    """Test user update"""
    # Create then update
    create_resp = client.post('/users', json={'name': 'Old Name', 'email': 'update@example.com'})
    user_id = json.loads(create_resp.data)['id']

    update_resp = client.put(f'/users/{user_id}',
                             json={'name': 'New Name', 'email': 'updated@example.com'})
    assert update_resp.status_code == 200

    # Verify update
    get_resp = client.get(f'/users/{user_id}')
    data = json.loads(get_resp.data)
    assert data['name'] == 'New Name'


def test_delete_user(client):
    """Test user deletion"""
    create_resp = client.post('/users',
                              json={'name': 'To Delete', 'email': 'delete@example.com'})
    user_id = json.loads(create_resp.data)['id']

    delete_resp = client.delete(f'/users/{user_id}')
    assert delete_resp.status_code == 200

    # Verify deletion
    get_resp = client.get(f'/users/{user_id}')
    assert get_resp.status_code == 404