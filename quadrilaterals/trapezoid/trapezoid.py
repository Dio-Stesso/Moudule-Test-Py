import math
import uuid

from quadrilaterals.quadrilateral import Quadrilateral


class Trapezoid(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._type = 'Trapezoid'
        self._id = uuid.uuid4()

        if not self.is_trapezoid():
            raise ValueError("The given vertices do not form a trapezoid.")

    def is_trapezoid(self):
        return self.is_parallel(self._vertices[0], self._vertices[1], self._vertices[2], self._vertices[3]) or \
            self.is_parallel(self._vertices[1], self._vertices[2], self._vertices[3], self._vertices[0])

    def is_parallel(self, p1, p2, p3, p4):
        vector1 = (p2[0] - p1[0], p2[1] - p1[1])
        vector2 = (p4[0] - p3[0], p4[1] - p3[1])
        return vector1[0] * vector2[1] == vector1[1] * vector2[0]

    def calculate_area(self):
        base1 = self._sides[0]
        base2 = self._sides[2]
        height = math.sin(self.angle_between(self._vertices[0], self._vertices[1], self._vertices[3])) * self._sides[1]
        return 0.5 * (base1 + base2) * height

    def calculate_angles(self):
        angles = []
        n = len(self._vertices)
        for i in range(n):
            angle = self.angle_between(self._vertices[i - 1], self._vertices[i], self._vertices[(i + 1) % n])
            angles.append(angle)
        return angles

    def angle_between(self, p1, p2, p3):
        vector1 = (p2[0] - p1[0], p2[1] - p1[1])
        vector2 = (p3[0] - p2[0], p3[1] - p2[1])
        return super().angle_between_vectors(vector1, vector2)

    def get_subtypes(self):
        return ["RightTrapezoid", "IsoscelesTrapezoid"]

    def get_supertypes(self):
        return [base.__name__ for base in self.__class__.__mro__[1:-2]]
