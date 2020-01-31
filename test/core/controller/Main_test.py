from src import app
import json


def test_main_page():
    client = app.test_client()
    response = client.get("/")
    json_data = json.loads(response.data)
    assert response.status_code == 200
    assert json_data["message"] == "ok"
