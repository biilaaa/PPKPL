import pytest


class TestCreateNote:
    def test_returns_201_with_valid_payload(self, client):
        r = client.post("/notes/", json={"title": "T1", "content": "C1"})
        assert r.status_code == 201
        data = r.json()
        assert data["title"] == "T1"
        assert data["content"] == "C1"
        assert "id" in data

    def test_auto_increments_id(self, client):
        r1 = client.post("/notes/", json={"title": "A", "content": "a"})
        r2 = client.post("/notes/", json={"title": "B", "content": "b"})
        assert r2.json()["id"] > r1.json()["id"]

    def test_returns_422_when_title_missing(self, client):
        r = client.post("/notes/", json={"content": "no title"})
        assert r.status_code == 422

    def test_returns_422_when_content_missing(self, client):
        r = client.post("/notes/", json={"title": "no content"})
        assert r.status_code == 422

    def test_returns_422_when_body_empty(self, client):
        r = client.post("/notes/", json={})
        assert r.status_code == 422

    def test_allows_empty_string_title(self, client):
        r = client.post("/notes/", json={"title": "", "content": "c"})
        assert r.status_code == 201
        assert r.json()["title"] == ""


class TestListNotes:
    def test_returns_empty_list_initially(self, client):
        r = client.get("/notes/")
        assert r.status_code == 200
        assert r.json() == []

    def test_returns_all_created_notes(self, client):
        client.post("/notes/", json={"title": "A", "content": "a"})
        client.post("/notes/", json={"title": "B", "content": "b"})
        client.post("/notes/", json={"title": "C", "content": "c"})
        r = client.get("/notes/")
        assert r.status_code == 200
        assert len(r.json()) == 3

    def test_each_note_has_expected_fields(self, client):
        client.post("/notes/", json={"title": "X", "content": "Y"})
        item = client.get("/notes/").json()[0]
        assert set(item.keys()) == {"id", "title", "content"}


class TestGetNote:
    def test_returns_created_note_by_id(self, client):
        created = client.post("/notes/", json={"title": "T", "content": "C"}).json()
        r = client.get(f"/notes/{created['id']}")
        assert r.status_code == 200
        assert r.json() == created

    def test_returns_404_for_nonexistent_id(self, client):
        r = client.get("/notes/9999")
        assert r.status_code == 404
        assert r.json()["detail"] == "Note not found"

    def test_returns_422_for_non_integer_id(self, client):
        r = client.get("/notes/abc")
        assert r.status_code == 422


class TestSearchNotes:
    def test_returns_all_notes_when_q_is_absent(self, client):
        client.post("/notes/", json={"title": "A", "content": "a"})
        client.post("/notes/", json={"title": "B", "content": "b"})
        r = client.get("/notes/search/")
        assert r.status_code == 200
        assert len(r.json()) == 2

    def test_matches_title(self, client):
        client.post("/notes/", json={"title": "Python guide", "content": "x"})
        client.post("/notes/", json={"title": "Java guide", "content": "x"})
        r = client.get("/notes/search/", params={"q": "Python"})
        assert r.status_code == 200
        results = r.json()
        assert len(results) == 1
        assert results[0]["title"] == "Python guide"

    def test_matches_content(self, client):
        client.post("/notes/", json={"title": "N1", "content": "secret keyword"})
        client.post("/notes/", json={"title": "N2", "content": "nothing here"})
        r = client.get("/notes/search/", params={"q": "secret"})
        assert len(r.json()) == 1

    def test_returns_empty_list_for_no_match(self, client):
        client.post("/notes/", json={"title": "A", "content": "a"})
        r = client.get("/notes/search/", params={"q": "zzzzz"})
        assert r.status_code == 200
        assert r.json() == []

    def test_partial_match(self, client):
        client.post("/notes/", json={"title": "Meeting notes", "content": "c"})
        r = client.get("/notes/search/", params={"q": "Meet"})
        assert len(r.json()) == 1

    def test_returns_all_when_q_is_empty_string(self, client):
        client.post("/notes/", json={"title": "A", "content": "a"})
        r = client.get("/notes/search/", params={"q": ""})
        assert r.status_code == 200
        assert len(r.json()) == 1
