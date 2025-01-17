def filter_data(students, min_height, min_weight):
    filtered_students = {name: (height, weight) for name, (height, weight) in students.items() if height > min_height and weight > min_weight}
    return filtered_students
