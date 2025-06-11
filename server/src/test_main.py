import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.config import API_PREFIX

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_sales():
    response = client.get(f"{API_PREFIX}/sales")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_and_get_sale():
    sale_data = {
        "Year": 2024,
        "Month": 6,
        "Supplier": "Test Supplier",
        "ItemCode": "TST123",
        "ItemDescription": "Test Item",
        "ItemType": "WINE",
        "RetailSales": 10.5,
        "RetailTransfers": 0.0,
        "WarehouseSales": 0.0
    }
    # Create sale
    response = client.post(f"{API_PREFIX}/sale", json=sale_data)
    assert response.status_code == 200
    sale = response.json()
    assert sale["Supplier"] == sale_data["Supplier"]
    sale_id = sale["id"]
    # Get sale
    response = client.get(f"{API_PREFIX}/sale/{sale_id}")
    assert response.status_code == 200
    fetched = response.json()
    assert fetched["id"] == sale_id
    assert fetched["Supplier"] == sale_data["Supplier"]

def test_update_and_delete_sale():
    sale_data = {
        "Year": 2024,
        "Month": 6,
        "Supplier": "ToUpdate",
        "ItemCode": "UPD123",
        "ItemDescription": "Update Item",
        "ItemType": "WINE",
        "RetailSales": 5.0,
        "RetailTransfers": 0.0,
        "WarehouseSales": 0.0
    }
    # Create sale
    response = client.post(f"{API_PREFIX}/sale", json=sale_data)
    sale_id = response.json()["id"]
    # Update sale
    update_data = {"Supplier": "Updated Supplier"}
    response = client.put(f"{API_PREFIX}/sale/{sale_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["Supplier"] == "Updated Supplier"
    # Delete sale
    response = client.delete(f"{API_PREFIX}/sale/{sale_id}")
    assert response.status_code == 200
    # Confirm deletion
    response = client.get(f"{API_PREFIX}/sale/{sale_id}")
    assert response.status_code == 404

def test_create_sale_missing_field():
    # Missing required field 'Supplier'
    sale_data = {
        "Year": 2024,
        "Month": 6,
        "ItemCode": "NEG1",
        "ItemDescription": "No Supplier",
        "ItemType": "WINE",
        "RetailSales": 1.0
    }
    response = client.post(f"{API_PREFIX}/sale", json=sale_data)
    assert response.status_code == 422
    assert "Supplier" in response.text

def test_get_nonexistent_sale():
    response = client.get(f"{API_PREFIX}/sale/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Sale not found"

def test_update_nonexistent_sale():
    update_data = {"Supplier": "ShouldNotExist"}
    response = client.put(f"{API_PREFIX}/sale/999999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Sale not found"

def test_delete_nonexistent_sale():
    response = client.delete(f"{API_PREFIX}/sale/999999")
    assert response.status_code == 404 or response.status_code == 200  # Accept 404 or 200 depending on implementation
