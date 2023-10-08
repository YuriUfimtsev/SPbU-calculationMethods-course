from math import exp


def f(x):
    return exp(7.5 * x)



def form_function_derivatives_table(default_function_table):
    result_table = [[0.0] * 8 for _ in range(len(default_function_table))]
    _copy_default_function_table_values(default_function_table, result_table)



def _copy_default_function_table_values(default_function_table, result_derivatives_table):
    for i in range(len(default_function_table)):
        for j in range(len(default_function_table[0])):
            result_derivatives_table[i][j] = default_function_table[i][j]