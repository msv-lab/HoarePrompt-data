def filter_data(student_dict, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in student_dict.items() if height >= min_height and weight >= min_weight}

# Test cases
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70) == {'Cierra Vega': (6.2, 70)}
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},5.9,67) == {'Cierra Vega': (6.2, 70),'Kierra Gentry': (6.0, 68)}
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},5.7,64) == {'Cierra Vega': (6.2, 70),'Alden Cantrell': (5.9, 65),'Kierra Gentry': (6.0, 68),'Pierre Cox': (5.8, 66)}
