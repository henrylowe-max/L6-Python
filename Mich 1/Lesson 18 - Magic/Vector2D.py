import math

class Vector2D:

    def __init__(self, x=0, y=0):

        self.x = x

        self.y = y

    def __repr__(self):

        return f"Vector2D({self.x!r}, {self.y!r})"

    def __abs__(self):

        return math.hypot(self.x, self.y)

    def __add__(self, other):

        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):

        return Vector2D(self.x * scalar, self.y * scalar)

v1 = Vector2D(2, 4)

v2 = Vector2D(2, 1)

print(v1 + v2) # Vector2D(4, 5)
print(abs(v1)) # 4.47213595499958
print(v1 * 3) # Vector2D(6, 12)