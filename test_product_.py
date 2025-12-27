from product import Product, ProductManager

def test_add_product():
    m = ProductManager()
    p = Product(1, 100)
    m.add(p)
    assert m.products[1].price == 100

def test_update_product():
    m = ProductManager()
    p = Product(1, 100)
    m.add(p)
    assert m.update(1, 150) is True
