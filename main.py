from circle import Circle
from test import Test
from product import Product

if __name__ == "__main__":
  # Introduction to class attributes

  # print(Circle.__dict__)
  # print(Circle.pi)

  # circle = Circle(10)
  # print(circle.__dict__)
  # print(circle.pi)
  # print(circle.area())
  # print(circle.circumference())

  # How Python class attributes work

  print(Test.x)

  test = Test()
  print(test.x)

  # When to use Python class attributes

  # 1) Storing class constants

  print(Circle.PI)

  # 2) Tracking data across of all instances

  Circle(10)
  Circle(20)
  print(len(Circle.circles))

  # 3) Defining default values

  product = Product(100)
  print(product.net_price())

  product = Product(100)
  product.set_discount(0.05)
  print(product.net_price())
