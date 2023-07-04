from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_api_people_full():
    response = client.post(
        "/graphql",
        json={"query": "query { people { email name address { number street city state } }}"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": {
            "people": [
                {
                    "email": "costa@person.com",
                    "name": "Costa",
                    "address": {
                        "number": 123,
                        "street": "Fake Street",
                        "city": "Springfield",
                        "state": "NSW",
                    },
                },
                {
                    "email": "jake@person.com",
                    "name": "Jake",
                    "address": {
                        "number": 99,
                        "street": "Ned Lane",
                        "city": "Shelbyville",
                        "state": "VIC",
                    },
                },
                {
                    "email": "sarah@person.com",
                    "name": "Sarah",
                    "address": {
                        "number": 1,
                        "street": "Krusty Avenue",
                        "city": "Ogdenville",
                        "state": "QLD",
                    },
                },
            ]
        }
    }
