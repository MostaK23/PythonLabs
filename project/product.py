class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_product_quality(self):
        return self.price / self.quantity

    def show_info(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Quality:", self.get_product_quality())
