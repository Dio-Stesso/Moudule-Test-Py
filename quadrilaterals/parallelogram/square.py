import uuid

from quadrilaterals.parallelogram.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._type = 'Square'
        self._id = uuid.uuid4()
        if not self._is_square():
            raise ValueError("The given vertices do not form a square.")

    def _is_square(self):
        side_length = self._sides[0]
        return all(side == side_length for side in self._sides)

    def get_subtypes(self):
        return []

    def get_supertypes(self):
        return [base.__name__ for base in self.__class__.__mro__[1:-2]]

    def is_type(self, type_name):
        type_hierarchy = ["Square", "Rectangle", "Parallelogram", "Quadrilateral"]
        return type_name in type_hierarchy
