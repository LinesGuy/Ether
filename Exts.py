import math

def interpolate(start, end, value):
    return start + (end - start) * value

def normalise_vector2(v):
    norm = v[0] ** 2 + v[1] ** 2
    if norm > 1:
        v = [i / norm for i in v]
    
    return v

def vector2_to_angle(v):
    return math.atan2(v[1], v[0])

#class vector2(object):

#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
    
#    def normalise(self):
#        # Returns a normalised unit vector
#        norm = math.sqrt(self.x*self.x + self.y*self.y)
#        x /= norm
#        y /= norm
#        return self.__class__(x, y)
    
#    def tuple(self):
#        # Returns the vector as a tuple (x, y)
#        return tuple(self.x, self.y)
