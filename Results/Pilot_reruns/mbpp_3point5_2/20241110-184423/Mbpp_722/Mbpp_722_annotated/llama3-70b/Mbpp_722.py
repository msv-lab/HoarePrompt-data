def filter_data(student_data, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in student_data.items() if height >= min_height and weight >= min_weight}
