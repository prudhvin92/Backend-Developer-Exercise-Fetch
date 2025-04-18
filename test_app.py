import pytest
from app import app, calculate_points

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_point_calculation():
    receipt = {
        "retailer": "Target",
        "total": "35.35",
        "items": [
            {"shortDescription": "Mtn Dew 12PK", "price": "6.49"},
            {"shortDescription": "Emils Pizza", "price": "12.25"}
        ],
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01"
    }
    assert calculate_points(receipt) >= 25  # Should be 28

def test_api(client):
    response = client.post('/receipts/process', json={
        "retailer": "Walmart",
        "total": "15.00",
        "items": [
            {"shortDescription": "Bread", "price": "3.00"}
        ],
        "purchaseDate": "2023-01-01",
        "purchaseTime": "14:00"
    })
    assert response.status_code == 200
    assert "id" in response.json
