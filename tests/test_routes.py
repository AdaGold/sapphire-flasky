def test_get_all_animals_with_empty_db_returns_empty_list(client):
    # ARRANGE IS INSIDE CONFTEST
    # ACT
    response = client.get('/animals')
    response_body = response.get_json()

    # ASSERT
    assert response_body == []
    assert response.status_code == 200


def test_get_all_animals_with_populated_db(client, three_animals):
    # ACT
    response = client.get('/animals')
    response_body = response.get_json()

    # ASSERT
    assert response.status_code == 200
    assert response_body == [
        {   
            "id": 1,
            "name": "Furby",
            "species": "Cat",
            "age": 17
        },
        {
            "id": 2,
            "name": "Gouda",
            "species": "Cheese Monster",
            "age": 14
        },
        {
            "id": 3,
            "name": "Foxy",
            "species": "Flamingo",
            "age": 100
        }
    ]

def test_get_one_animal_empty_db_returns_404(client):
    response = client.get("/animals/1")
    assert response.status_code == 404

def test_returns_400_with_invalid_animal_id(client):
    response = client.get("/animals/Furby")
    assert response.status_code == 400

def test_post_one_animal_creates_animal_in_db(client):
    response = client.post("/animals", json={
        "name": "Clifford",
        "species": "BIG dog",
        "age": 2
        }
    )

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body["id"] == 1
    assert response_body["name"] == "Clifford"
    assert "msg" in response_body

def test_update_one_animal_updates_animal_in_db(client, three_animals):
    response = client.put("/animals/3", json={
        "name": "Foxy fox",
        "species": "Fox",
        "age": 200
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == 3
    assert response_body["name"] == "Foxy fox"
    assert response_body["species"] == "Fox"

def test_get_one_valid_animal_in_db(client, three_animals):
    # ACT
    response = client.get('/animals/1')
    response_body = response.get_json()

    # ASSERT
    assert response.status_code == 200
    assert response_body["id"] == 1
    assert response_body["name"] == "Furby"
    assert response_body["species"] == "Cat"
    assert response_body["age"] == 17