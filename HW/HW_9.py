# Write Abstract class Figure
# Inherit Triangle and Round from it
# Create a collection of Figures, count perimeter and square of them

from abc import ABC, abstractmethod
import math
class Figure(ABC):
    @abstractmethod
    def __init__(self, perimeter, area):
        self.perimeter = perimeter
        self.area = area
    # @abstractmethod

class Triangle(Figure):
    def __init__(self, triangle_side):
        self.triangle_side = triangle_side

    def perimeter(self):
        return self.triangle_side * 3

    def area(self):
        (self.triangle_side ** 2 * math.sqrt(3)) / 4

class Round(Figure):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

figures_collection = [
    Triangle(5),
    Round(5),
    Round(22)
]

for figures in figures_collection:
    print(f'Perimeter - {figures.perimeter()} ')
    print(f'Area - {figures.area()} ')





