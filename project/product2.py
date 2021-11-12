from datetime import datetime
from product import Product


class Product2(Product):

    def __init__(self, name: str, price: float, quantity: int, year_of_issue: int):
        super().__init__(name, price, quantity)
        self.year_of_issue = year_of_issue
        self.current_year = datetime.now().year

    def get_product_quality(self):
        return super().get_product_quality() + 0.5 * (self.current_year - self.year_of_issue)
