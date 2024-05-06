class Product:
  DEFAULT_DISCOUNT = 0

  def __init__(self, price):
    self.price = price
    self.discount = Product.DEFAULT_DISCOUNT

  def set_discount(self, discount):
    self.discount = discount

  def net_price(self):
    return self.price * (1 - self.discount)
