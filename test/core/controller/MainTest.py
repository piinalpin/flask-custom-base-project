from src import app
import json


def test_main_page():
    client = app.test_client()
    response = client.get("/")
    json_data = json.loads(response.data)
    assert response.status_code == 200
    assert json_data["message"] == "ok"


# def test_oauth_authorized():
#     client = app.test_client()
#     headers = {
#         "Authorization": "Basic aHl1Z2E6aGluYXRh"
#     }
#     data = "username=admin&password=password"
#     response = client.post("/oauth/token", headers=headers, data=data, content_type='application/x-www-form-urlencoded')
#     assert response.status_code == 200
