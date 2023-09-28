
class Node:
    def __init__(self, name: str, long: float, lat: float):
        self.id = name
        self.longitude = long
        self.latitude = lat
        self.h = 0

    def __str__(self):
        return self.id

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
