# test_product_sales.py
from product_sales import process_sale

def test_default_product_sale():
    output = process_sale()

    assert "Product ID: 1001" in output
    assert "Product Name: Default Laptop" in output
    assert "Product Price: 45000" in output
    assert "Product Stock: 8" in output
