import pytest


class TestCreateActionItem:
    def test_returns_201_with_valid_payload(self, client):
        r = client.post("/action-items/", json={"description": "Ship it"})
        assert r.status_code == 201
        data = r.json()
        assert data["description"] == "Ship it"
        assert data["completed"] is False
        assert "id" in data

    def test_auto_increments_id(self, client):
        r1 = client.post("/action-items/", json={"description": "A"})
        r2 = client.post("/action-items/", json={"description": "B"})
        assert r2.json()["id"] > r1.json()["id"]

    def test_returns_422_when_description_missing(self, client):
        r = client.post("/action-items/", json={})
        assert r.status_code == 422

    def test_returns_422_when_body_is_not_json(self, client):
        r = client.post("/action-items/", content=b"not json", headers={"Content-Type": "application/json"})
        assert r.status_code == 422

    def test_allows_empty_string_description(self, client):
        r = client.post("/action-items/", json={"description": ""})
        assert r.status_code == 201
        assert r.json()["description"] == ""

    def test_completed_defaults_to_false(self, client):
        r = client.post("/action-items/", json={"description": "task"})
        assert r.json()["completed"] is False


class TestListActionItems:
    def test_returns_empty_list_initially(self, client):
        r = client.get("/action-items/")
        assert r.status_code == 200
        assert r.json() == []

    def test_returns_all_created_items(self, client):
        client.post("/action-items/", json={"description": "A"})
        client.post("/action-items/", json={"description": "B"})
        r = client.get("/action-items/")
        assert r.status_code == 200
        assert len(r.json()) == 2

    def test_each_item_has_expected_fields(self, client):
        client.post("/action-items/", json={"description": "X"})
        item = client.get("/action-items/").json()[0]
        assert set(item.keys()) == {"id", "description", "completed"}

    def test_includes_both_completed_and_incomplete(self, client):
        r1 = client.post("/action-items/", json={"description": "done"}).json()
        client.post("/action-items/", json={"description": "pending"})
        client.put(f"/action-items/{r1['id']}/complete")

        items = client.get("/action-items/").json()
        statuses = {item["completed"] for item in items}
        assert statuses == {True, False}


class TestCompleteActionItem:
    def test_marks_item_as_completed(self, client):
        item = client.post("/action-items/", json={"description": "do it"}).json()
        r = client.put(f"/action-items/{item['id']}/complete")
        assert r.status_code == 200
        assert r.json()["completed"] is True

    def test_preserves_description_after_completing(self, client):
        item = client.post("/action-items/", json={"description": "important"}).json()
        r = client.put(f"/action-items/{item['id']}/complete")
        assert r.json()["description"] == "important"

    def test_completing_already_completed_item_stays_completed(self, client):
        item = client.post("/action-items/", json={"description": "x"}).json()
        client.put(f"/action-items/{item['id']}/complete")
        r = client.put(f"/action-items/{item['id']}/complete")
        assert r.status_code == 200
        assert r.json()["completed"] is True

    def test_returns_404_for_nonexistent_id(self, client):
        r = client.put("/action-items/9999/complete")
        assert r.status_code == 404
        assert r.json()["detail"] == "Action item not found"

    def test_returns_422_for_non_integer_id(self, client):
        r = client.put("/action-items/abc/complete")
        assert r.status_code == 422
