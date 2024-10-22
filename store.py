class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        """Adds a new product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total number of items in the store."""
        total_quantity = sum(product.get_quantity() for product in self.products if product.is_active())
        return total_quantity

    def get_all_products(self):
        """Returns all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """Processes an order and returns the total price."""
        total_price = 0.0
        for product, quantity in shopping_list:
            if product.is_active():
                total_price += product.buy(quantity)
            else:
                raise Exception(f"{product.name} is not available for purchase.")
        return total_price


