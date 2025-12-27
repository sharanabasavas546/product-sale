# test_product_sales.py
from product_sale import process_sale

def test_successful_sale():
    output = process_sale(101, "Laptop", 50000, 5, 2)

    expected_output = (
        "Product ID: 101\n"
        "Product Name: Laptop\n"
        "Product Price: 50000\n"
        "Product Stock: 3\n"
        "Total Sale Amount: 100000"
    )

    assert output == expected_output


def test_insufficient_stock():
    output = process_sale(102, "Mobile", 20000, 1, 3)

    expected_output = (
        "Product ID: 102\n"
        "Product Name: Mobile\n"
        "Product Price: 20000\n"
        "Product Stock: 1\n"
        "Status: Insufficient Stock"
    )

    assert output == expected_output
