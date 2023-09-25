import polynomial as pol


class NewtonInterpolator:
    def __init__(self):
        self.table = [[0.0] for _ in range(2)]
        self.polynomial = pol.Polynomial(1)

    def _form_polynomial(self, polynomial_degree):
        def get_pol_multiplier(degree_number):
            multiplier = pol.Polynomial(1)
            for p in range(0, degree_number):
                multiplier *= pol.Polynomial(1, -1 * self.table[p * 2][0])
            return multiplier

        result = self.table[0][1] * pol.Polynomial(1)
        for i in range(1, polynomial_degree + 1):
            result += self.table[i][i + 1] * get_pol_multiplier(i)
        self.polynomial = result

    def reform_separated_differences_table(self, points, function_in_points):
        self.table = [[0.0] * (len(points) + 1) for _ in range(len(points) * 2 - 1)]
        for i in range(0, len(self.table), 2):
            self.table[i][0] = points[i // 2]
            self.table[i][1] = function_in_points[i // 2]

        row_offset = 0
        for k in range(2, len(self.table[0]), 1):
            row_offset += 1
            for i in range(row_offset, len(self.table) - row_offset, 2):
                self.table[i][k] = ((self.table[i + 1][k - 1] - self.table[i - 1][k - 1])
                                    / (self.table[i + (k - 1)][0] - self.table[i - (k - 1)][0]))

    def calculate_polynomial_value_at_point(self, polynomial_degree, x):
        if polynomial_degree != self.polynomial.degree:
            self._form_polynomial(polynomial_degree)
        return self.polynomial.calculate(x)