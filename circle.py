class Circle:
  circles = []
  PI = 3.14159

  def __init__(self, radius):
    self.radius = radius
    Circle.circles.append(self)

  def area(self):
    return Circle.PI * self.radius ** 2

  def circumference(self):
    return 2 * Circle.PI * self.radius
