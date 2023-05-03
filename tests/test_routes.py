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
