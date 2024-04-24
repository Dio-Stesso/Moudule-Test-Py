import uuid

from quadrilaterals.trapezoid.trapezoid import Trapezoid


class IsoscelesTrapezoid(Trapezoid):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._type = 'IsoscelesTrapezoid'
        self._id = uuid.uuid4()
        if not self.is_isosceles():
            raise ValueError("The given vertices do not form an isosceles trapezoid")

    def is_isosceles(self):
        # Check that the non-parallel sides are equal
        non_parallel_sides = []
        if not self.is_parallel(self._vertices[0], self._vertices[1], self._vertices[2], self._vertices[3]):
            non_parallel_sides.append(self.distance(self._vertices[0], self._vertices[1]))
            non_parallel_sides.append(self.distance(self._vertices[2], self._vertices[3]))
        if not self.is_parallel(self._vertices[1], self._vertices[2], self._vertices[3], self._vertices[0]):
            non_parallel_sides.append(self.distance(self._vertices[1], self._vertices[2]))
            non_parallel_sides.append(self.distance(self._vertices[3], self._vertices[0]))

        return len(set(non_parallel_sides)) == 1

    def calculate_area(self):
        return super().calculate_area()

    def get_subtypes(self):
        return []

    def get_supertypes(self):
        return [base.__name__ for base in self.__class__.__mro__[1:-2]]
