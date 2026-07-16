from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"



def test_add():
    client = app.test_client()
    response = client.get("/add/2/3")
    assert response.get_json()["result"] == 5



def test_add_negative():
    client = app.test_client()
    response = client.get("/add/-5/10")
    assert response.get_json()["result"] == 5
