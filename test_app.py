import pytest
from app import app, calculate_points

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_target_receipt():
    receipt = {
        "retailer": "Target",
        "total": "35.35",
        "items": [
            {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
            {"shortDescription": "Emils Cheese Pizza", "price": "12.25"}
        ],
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01"
    }
    assert calculate_points(receipt) == 28  # Verify exact point value
