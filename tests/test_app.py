import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Suponiendo que existe una actividad llamada 'Chess Club'
    activity_name = "Chess Club"
    email = "testuser@mergington.edu"

    # Signup
    signup = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup.status_code in (200, 400)  # Puede estar ya inscrito

    # Signup duplicado debe fallar
    signup2 = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup2.status_code == 400

    # Unregister
    unregister = client.post(f"/activities/{activity_name}/unregister?email={email}")
    assert unregister.status_code == 200

    # Unregister de nuevo debe fallar
    unregister2 = client.post(f"/activities/{activity_name}/unregister?email={email}")
    assert unregister2.status_code == 400
