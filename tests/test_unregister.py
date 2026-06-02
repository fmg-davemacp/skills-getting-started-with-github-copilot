from src.app import activities


def test_unregister_removes_participant(client):
    response = client.delete("/activities/Chess Club/participants/michael@mergington.edu")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Unregistered michael@mergington.edu from Chess Club"
    }
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_unregister_rejects_unknown_activity(client):
    response = client.delete("/activities/Unknown Club/participants/student@mergington.edu")

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_rejects_missing_participant(client):
    response = client.delete("/activities/Chess Club/participants/student@mergington.edu")

    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found in this activity"}