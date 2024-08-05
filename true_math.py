from math import inf


def divide(first, second):
    if second == 0 and first > 0:
        return inf
    if second == 0 and first < 0:
        return -inf
    else:
        result = first / second
        return result



