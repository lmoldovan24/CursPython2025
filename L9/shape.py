import math


class ShapeError(Exception):
    """Clasă de bază pentru erori legate de forme."""
    pass

class InvalidDimensionError(ShapeError):
    """Dimensiuni invalide (<= 0 sau tip greșit)."""
    pass

class Shape:
    def area(self):
        raise NotImplementedError("Metoda area() trebuie implementată în subclasă.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = self._validate_dimension(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return (
            f"Circle with radius {self.radius} "
            f"has area {self.area():.2f}"
        )

    @staticmethod
    def _validate_dimension(value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise InvalidDimensionError("Dimensiunea trebuie să fie un număr.")
        if value <= 0:
            raise InvalidDimensionError("Dimensiunea trebuie să fie > 0.")
        return float(value)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = self._validate_dimension(width)
        self.height = self._validate_dimension(height)

    def area(self):
        return self.width * self.height

    def __str__(self):
        return (
            f"Rectangle with width {self.width} and height {self.height} "
            f"has area {self.area():.0f}"
        )

    @staticmethod
    def _validate_dimension(value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise InvalidDimensionError("Dimensiunea trebuie să fie un număr.")
        if value <= 0:
            raise InvalidDimensionError("Dimensiunea trebuie să fie > 0.")
        return float(value)

if __name__ == "__main__":
    try:
        circle = Circle(5)
        rectangle = Rectangle(10, 4)

        print(circle)
        print(rectangle)

    except InvalidDimensionError as e:
        print("Eroare dimensiuni:", e)
    except ShapeError as e:
        print("Eroare formă:", e)
