from copy import deepcopy

class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "[ "+str(self.x)+", "+str(self.y)+", "+str(self.z)+" ]"
    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Vector3(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Vector3(self.x-other.x, self.y-other.y, self.z-other.z)

    def copy(self):
        return deepcopy(self)

    def magnitudeSquared(self):
        return (self.x*self.x + self.y*self.y + self.z*self.z)