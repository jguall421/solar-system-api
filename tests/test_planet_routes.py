def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, one_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "description": "Our home planet",
        "size":"Medium"
    }

def test_get_one_planet_not_found(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": " planet1 not found"
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Sun",
        "size": "huge",
        "description": "Sun heat"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Sun",
        "size": "huge",
        "description": "Sun heat"
    }