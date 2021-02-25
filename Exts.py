"""Various quality-of-life functions"""

def interpolate(start, end, value):
    """Linearly interpolates between two values"""
    return start + (end - start) * value
