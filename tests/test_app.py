from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_signup_for_activity_success():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    activities[activity_name]["participants"] = [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]

    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    assert response.status_code == 200
    assert email in activities[activity_name]["participants"]


def test_student_cannot_sign_up_twice_for_same_activity():
    activity_name = "Chess Club"
    email = "duplicate@mergington.edu"

    activities[activity_name]["participants"] = [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]

    first_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    second_response = client.post(f"/activities/{activity_name}/signup?email={email}")

    assert first_response.status_code == 200
    assert second_response.status_code == 400
    assert activities[activity_name]["participants"].count(email) == 1
