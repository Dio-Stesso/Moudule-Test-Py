import math
from abc import ABC, abstractmethod
import uuid


class Quadrilateral(ABC):
    def __init__(self, vertices):
        self._type = self.__class__.__name__  # Figure type, e.g. "Rectangle"
        if len(vertices) != 4:
            raise ValueError("A figure must have 4 vertices.")
        self._id = uuid.uuid4()
        self._vertices = tuple(vertices)
        self._sides = self.calculate_sides()
        self._perimeter = self.calculate_perimeter()
        self._area = self.calculate_area()
        self._diagonals = self.calculate_diagonals()
        self._angles = self.calculate_angles()

    @abstractmethod
    def calculate_sides(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_diagonals(self):
        pass

    @abstractmethod
    def calculate_angles(self):
        pass

    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id

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

    def is_type(self, type_name):
        return self._type == type_name

    def compare_by_area(self, other):
        if not isinstance(other, Quadrilateral):
            return NotImplemented
        return self._area - other.area

    def distance(self, p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def compare_by_perimeter(self, other):
        if not isinstance(other, Quadrilateral):
            return NotImplemented
        return self._perimeter - other.perimeter

    def compare_by_area_and_perimeter(self, other):
        return self.compare_by_area(other), self.compare_by_perimeter(other)

    def check_intersection(self, other):
        if not isinstance(other, Quadrilateral):
            return NotImplemented

        def do_lines_intersect(line1, line2):
            def ccw(A, B, C):
                return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

            A, B = line1
            C, D = line2
            return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

        for i in range(len(self._vertices)):
            line1 = (self._vertices[i], self._vertices[(i + 1) % len(self._vertices)])
            for j in range(len(other.vertices)):
                line2 = (other.vertices[j], other.vertices[(j + 1) % len(other.vertices)])
                if do_lines_intersect(line1, line2):
                    return True
        return False

    def angle_between_vectors(self, vector1, vector2):
        dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        magnitude1 = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
        magnitude2 = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)
        cos_theta = dot_product / (magnitude1 * magnitude2)
        angle = math.acos(cos_theta) * (180 / math.pi)
        return angle

    def is_vectors_perpendicular(self, vector1, vector2):
        return vector1[0] * vector2[0] + vector1[1] * vector2[1] == 0
