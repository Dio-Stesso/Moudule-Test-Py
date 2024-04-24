import uuid

from quadrilaterals.quadrilateral import Quadrilateral


class Parallelogram(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._type = 'Parallelogram'
        self._id = uuid.uuid4()

        if not self._is_parallelogram():
            raise ValueError("The given vertices do not form a parallelogram.")

    def calculate_sides(self):
        return (
            self.distance(self._vertices[0], self._vertices[1]),
            self.distance(self._vertices[1], self._vertices[2]),
            self.distance(self._vertices[2], self._vertices[3]),
            self.distance(self._vertices[3], self._vertices[0])
        )

    def calculate_perimeter(self):
        return sum(self._sides)

    def calculate_area(self):
        p1, p2, p3, _ = self._vertices
        base_vector = (p2[0] - p1[0], p2[1] - p1[1])
        height_vector = (p3[0] - p2[0], p3[1] - p2[1])
        return abs(base_vector[0] * height_vector[1] - base_vector[1] * height_vector[0])

    def calculate_diagonals(self):
        return (
            self.distance(self._vertices[0], self._vertices[2]),
            self.distance(self._vertices[1], self._vertices[3])
        )

    def calculate_angles(self):
        if not self._is_parallelogram():
            raise ValueError("The given figure is not a parallelogram")

        angles = []
        n = len(self._vertices)
        for i in range(n):
            vector1 = (self._vertices[(i + 1) % n][0] - self._vertices[i][0],
                       self._vertices[(i + 1) % n][1] - self._vertices[i][1])
            vector2 = (self._vertices[(i - 1 + n) % n][0] - self._vertices[i][0],
                       self._vertices[(i - 1 + n) % n][1] - self._vertices[i][1])

            angle = super().angle_between_vectors(vector1, vector2)
            angles.append(angle)

        return angles

    def _is_parallelogram(self):
        return (self._sides[0] == self._sides[2]) and (self._sides[1] == self._sides[3])

    def get_subtypes(self):
        return ["Rectangle", "Square"]

    def get_supertypes(self):
        return [base.__name__ for base in self.__class__.__mro__[1:-2]]

    def is_type(self, type_name):
        type_hierarchy = ["Square", "Rectangle", "Parallelogram", "Quadrilateral"]
        return type_name in type_hierarchy
