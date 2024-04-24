import uuid

from quadrilaterals.parallelogram.parallelogram import Parallelogram


class Rhombus(Parallelogram):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._type = 'Rhombus'
        self._id = uuid.uuid4()

        if not self._is_rhombus():
            raise ValueError("The given vertices do not form a rhombus.")

    def _is_rhombus(self):
        first_side_length = self._sides[0]
        return all(side == first_side_length for side in self._sides)

    def calculate_area(self):
        d1, d2 = self.calculate_diagonals()
        return 0.5 * d1 * d2

    def calculate_angles(self):
        return super().calculate_angles()

    def get_supertypes(self):
        return [base.__name__ for base in self.__class__.__mro__[1:-2]]
