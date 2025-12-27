# product_sales.py

sales = []

def process_sale(product_id, product_name, product_price, product_stock, quantity=1):
    """
    Process a product sale and return formatted output.
    """

    if quantity <= product_stock:
        total = product_price * quantity
        remaining_stock = product_stock - quantity

        result = (
            f"Product ID: {product_id}\n"
            f"Product Name: {product_name}\n"
            f"Product Price: {product_price}\n"
            f"Product Stock: {remaining_stock}\n"
            f"Total Sale Amount: {total}"
        )

        sales.append(result)
        return result
    else:
        return (
            f"Product ID: {product_id}\n"
            f"Product Name: {product_name}\n"
            f"Product Price: {product_price}\n"
            f"Product Stock: {product_stock}\n"
            f"Status: Insufficient Stock"
        )
