import uuid

from quadrilaterals.parallelogram.parallelogram import Parallelogram


class Rectangle(Parallelogram):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._type = 'Rectangle'
        self._id = uuid.uuid4()
        self._vertices = tuple(vertices)
        if len(vertices) != 4:
            raise ValueError("A rectangle must have 4 vertices.")

        self._sides = self.calculate_sides()

        if not self._is_rectangle():
            raise ValueError("The given vertices do not form a rectangle.")

        self._perimeter = self.calculate_perimeter()
        self._area = self.calculate_area()
        self._diagonals = self.calculate_diagonals()
        self._angles = self.calculate_angles()

    def calculate_perimeter(self):
        return sum(self._sides)

    def calculate_area(self):
        return self._sides[0] * self._sides[1]

    def calculate_diagonals(self):
        return (
            self.distance(self._vertices[0], self._vertices[2]),
            self.distance(self._vertices[1], self._vertices[3]),
        )

    def calculate_angles(self):
        return 90, 90, 90, 90

    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return str(self._id)

    @property
    def vertices(self):
        return self._vertices

    @property
    def sides(self):
        return self._sides

    @property
    def perimeter(self):
        return self._perimeter

    @property
    def area(self):
        return self._area

    @property
    def diagonals(self):
        return self._diagonals

    @property
    def angles(self):
        return self._angles

    def get_subtypes(self):
        return ["Square"]

    def get_supertypes(self):
        return ["Quadrilateral", "Parallelogram"]

    def is_type(self, type_name):
        type_hierarchy = ["Rectangle", "Quadrilateral", "Parallelogram"]
        return type_name in type_hierarchy

    def _is_rectangle(self):
        if self._sides[0] != self._sides[2] or self._sides[1] != self._sides[3]:
            return False
        for i in range(len(self._vertices)):
            if not self._is_right_angle(i):
                return False
        return True

    def _is_right_angle(self, index):
        p1 = self._vertices[index]
        p2 = self._vertices[(index + 1) % 4]
        p3 = self._vertices[(index + 2) % 4]

        vector1 = (p2[0] - p1[0], p2[1] - p1[1])
        vector2 = (p3[0] - p2[0], p3[1] - p2[1])

        return super().is_vectors_perpendicular(vector1, vector2)
