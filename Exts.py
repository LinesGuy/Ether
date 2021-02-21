import math

def interpolate(start, end, value):
    return start + (end - start) * value

class vector2(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def normalise(self):
        # Returns a normalised unit vector
        norm = math.sqrt(self.x*self.x + self.y*self.y)
        x /= norm
        y /= norm
        return self.__class__(x, y)
