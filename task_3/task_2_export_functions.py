from math import exp


def f(x_):
    return 1 - exp(-x_) + x_ ** 2


def Lagrange(n_, z_, x):
    result = 0
    for k in range(n_ + 1):
        p1 = 1
        for i in range(n_ + 1):
            if i != k:
                p1 *= (x - z_[i][0])
        p2 = 1
        for i in range(n_ + 1):
            if i != k:
                p2 *= (z_[k][0] - z_[i][0])
        # result += f(z_[k]) * p1 / p2
        result += z_[k][1] * p1 / p2
    return result


def get_interpolation_table(a, h, points_count_, func):
    """
    Generates a table with interpolation nodes and function values in these nodes.
    Based on start of the segment and step.
    """
    return [(a + i * h,
             func(a + i * h)) for i in range(points_count_)]


def sort_interpolation_table(interpolation_table, x):
    """
    Sorts a table with interpolation nodes and function values in these nodes.
    Nodes are ordered by proximity to a point x.
    """
    return sorted(interpolation_table, key=lambda array: abs(array[0] - x))


def print_interpolation_table(interpolation_table):
    """
    Prints a table with interpolation nodes and function values in these nodes.
    """
    for j in range(len(interpolation_table)):
        print(f'f({interpolation_table[j][0]}) = {interpolation_table[j][1]}')
