def parse_coefficients(equation_string):
    left = equation_string.split(' = ')
    members = left.split(' + ').split(' - ')
    coefficients = []
    for item in members:
        coefficients.append(item.split(' * '))
    return coefficients