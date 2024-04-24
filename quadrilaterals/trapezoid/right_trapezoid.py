import math
import uuid

from quadrilaterals.trapezoid.trapezoid import Trapezoid


class RightTrapezoid(Trapezoid):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._type = 'RightTrapezoid'
        self._id = uuid.uuid4()
        if not self._is_right_trapezoid():
            raise ValueError("The given vertices do not form a right trapezoid.")

    def _is_right_trapezoid(self):
        # Check if exactly one pair of non-parallel sides is perpendicular
        perpendicular_count = 0
        for i in range(4):
            if self.is_perpendicular(self._vertices[i], self._vertices[(i+1) % 4], self._vertices[(i+1) % 4], self._vertices[(i+2) % 4]):
                perpendicular_count += 1
        return perpendicular_count == 1

    def is_perpendicular(self, p1, p2, p3, p4):
        vector1 = (p2[0] - p1[0], p2[1] - p1[1])
        vector2 = (p4[0] - p3[0], p4[1] - p3[1])
        return super().is_vectors_perpendicular(vector1, vector2)

    def calculate_area(self):
        bases = []
        for i in range(4):
            if self.is_parallel(self._vertices[i], self._vertices[(i+1) % 4], self._vertices[(i+2) % 4], self._vertices[(i+3) % 4]):
                bases.append(self.distance(self._vertices[i], self._vertices[(i+1) % 4]))
        if len(bases) != 2:
            return 0
        height = math.sin(self.angle_between(self._vertices[0], self._vertices[1], self._vertices[3])) * self._sides[1]
        return 0.5 * (bases[0] + bases[1]) * height

    def get_subtypes(self):
        return []

    def get_supertypes(self):
        return [base.__name__ for base in self.__class__.__mro__[1:-2]]
