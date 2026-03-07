def test_create_action_item_with_priority(client):
    payload = {"description": "High priority task", "priority": "high"}
    r = client.post("/action-items/", json=payload)
    assert r.status_code == 201, r.text
    item = r.json()
    assert item["priority"] == "high"
    assert item["description"] == "High priority task"
    assert item["completed"] is False

    r = client.get("/action-items/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 1
    assert items[0]["priority"] == "high"