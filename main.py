from circle import Circle

if __name__ == "__main__":
  # Introduction to class attributes

  print(Circle.__dict__)
  print(Circle.pi)

  circle = Circle(10)
  print(circle.__dict__)
  print(circle.pi)
  print(circle.area())
  print(circle.circumference())
