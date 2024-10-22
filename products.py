class Product:
    def __init__(self, name, quantity, price, active):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.active = active

    @property
    def get_quantity(self) -> int:
       return self._quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            return
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if quantity <= 0:
            return
        total_price = self.price * quantity
        return total_price




