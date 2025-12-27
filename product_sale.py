# product_sales.py

def process_sale(
    product_id=1001,
    product_name="Default Laptop",
    product_price=45000,
    product_stock=10,
    quantity=2
):
    if quantity <= product_stock:
        remaining_stock = product_stock - quantity
        total = product_price * quantity

        output = (
            f"Product ID: {product_id}\n"
            f"Product Name: {product_name}\n"
            f"Product Price: {product_price}\n"
            f"Product Stock: {remaining_stock}\n"
            f"Total Sale Amount: {total}\n"
        )

        print(output)   # 🔥 IMPORTANT: Jenkins will show this
        return output
    else:
        output = (
            f"Product ID: {product_id}\n"
            f"Product Name: {product_name}\n"
            f"Product Price: {product_price}\n"
            f"Product Stock: {product_stock}\n"
            f"Status: Insufficient Stock\n"
        )

        print(output)
        return output
