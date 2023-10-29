from math import exp


def f(x):
    return exp(7.5 * x)


def _f_first_derivative(x):
    return 7.5 * exp(7.5 * x)


def _f_second_derivative(x):
    return 7.5 * 7.5 * exp(7.5 * x)


def form_function_derivatives_table(default_function_table):
    result_table = [[0.0] * 10 for _ in range(len(default_function_table))]
    _copy_default_function_table_values(default_function_table, result_table)
    _h = result_table[1][0] - result_table[0][0]
    _fill_first_derivative_base_column(result_table)
    _fill_first_derivative_num_diff_column(result_table, _h)
    _fill_first_derivative_absolute_inaccuracy_column(result_table)
    _fill_first_derivative_relative_inaccuracy_column(result_table)
    _fill_second_derivative_base_column(result_table)
    _fill_second_derivative_num_diff_column(result_table, _h)
    _fill_second_derivative_absolute_inaccuracy_column(result_table)
    # _fill_second_derivative_relative_inaccuracy_column(result_table)
    return _create_string_matrix(result_table)


def _create_string_matrix(result_derivatives_table):
    header = [
        'x',
        'f(x)',
        'f\'(x) т.',
        'f\'(x) ч.д.',
        '|f\'(x) т. - f\'(x) ч.д.|',
        'Δ относ.',
        'f\'\'(x) т.',
        'f\'\'(x) ч.д.',
        '|f\'\'(x) т. - f\'\'(x) ч.д.|',
        'Δ относ.'
    ]
    result_matrix = []
    for row in result_derivatives_table:
        new_row = [str(number) for number in row]
        result_matrix.append(new_row)
    for i in range(7, 10):
        result_matrix[0][i] = ''
        result_matrix[len(result_derivatives_table) - 1][i] = ''
    result_matrix.insert(0, header)
    return result_matrix


def _copy_default_function_table_values(default_function_table, result_derivatives_table):
    for i in range(len(default_function_table)):
        for j in range(len(default_function_table[0])):
            result_derivatives_table[i][j] = default_function_table[i][j]


def _fill_first_derivative_base_column(result_derivatives_table):
    for i in range(len(result_derivatives_table)):
        result_derivatives_table[i][2] = _f_first_derivative(result_derivatives_table[i][0])


def _fill_first_derivative_num_diff_column(result_derivatives_table, h):
    for i in range(len(result_derivatives_table)):
        if i == 0:
            result_derivatives_table[i][3] = (
                    (-3 * result_derivatives_table[i][1]
                     + 4 * result_derivatives_table[i + 1][1]
                     - result_derivatives_table[i + 2][1])
                    / (2 * h)
            )
        elif i == len(result_derivatives_table) - 1:
            result_derivatives_table[i][3] = (
                    (3 * result_derivatives_table[i][1]
                     - 4 * result_derivatives_table[i - 1][1]
                     + result_derivatives_table[i - 2][1])
                    / (2 * h)
            )
        else:
            result_derivatives_table[i][3] = (
                    (result_derivatives_table[i + 1][1]
                     - result_derivatives_table[i - 1][1])
                    / (2 * h)
            )


def _fill_first_derivative_absolute_inaccuracy_column(result_derivatives_table):
    for i in range(len(result_derivatives_table)):
        result_derivatives_table[i][4] = abs(result_derivatives_table[i][3] - result_derivatives_table[i][2])


def _fill_first_derivative_relative_inaccuracy_column(result_derivatives_table):
    for i in range(len(result_derivatives_table)):
        result_derivatives_table[i][5] = result_derivatives_table[i][4] / abs(result_derivatives_table[i][3])


def _fill_second_derivative_base_column(result_derivatives_table):
    for i in range(len(result_derivatives_table)):
        result_derivatives_table[i][5 + 1] = _f_second_derivative(result_derivatives_table[i][0])


def _fill_second_derivative_num_diff_column(result_derivatives_table, h):
    for i in range(len(result_derivatives_table)):
        if i != 0 and i != (len(result_derivatives_table) - 1):
            result_derivatives_table[i][5 + 2] = (
                    (result_derivatives_table[i + 1][1]
                     - 2 * result_derivatives_table[i][1]
                     + result_derivatives_table[i - 1][1])
                    / h ** 2
            )


def _fill_second_derivative_absolute_inaccuracy_column(result_derivatives_table):
    for i in range(len(result_derivatives_table)):
        if i != 0 and i != (len(result_derivatives_table) - 1):
            result_derivatives_table[i][5 + 3] = (
                abs(result_derivatives_table[i][5 + 2] - result_derivatives_table[i][5 + 1]))


def _fill_second_derivative_relative_inaccuracy_column(result_derivatives_table):
    for i in range(len(result_derivatives_table)):
        if i != 0 and i != (len(result_derivatives_table) - 1):
            result_derivatives_table[i][5 + 4] = result_derivatives_table[i][5 + 3] / abs(
                result_derivatives_table[i][5 + 2])
