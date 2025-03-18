#State of the program right berfore the function call: student_data is a dictionary where each key is a student name and the corresponding value is a tuple of two floats (student_height, student_weight). min_height and min_weight are floats representing the minimal height and minimal weight respectively.**
def func_1(student_data, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in student_data.
    items() if height >= min_height and weight >= min_weight}
    #The program returns a dictionary where each key is a student name and the corresponding value is a tuple of two floats (student_height, student_weight) for students whose height is greater than or equal to min_height and weight is greater than or equal to min_weight.
#Overall this is what the function does:The function `func_1` accepts three parameters: `student_data`, `min_height`, and `min_weight`. `student_data` is a dictionary where each key is a student name and the corresponding value is a tuple of two floats (student_height, student_weight). The function filters the student data based on the criteria that the student's height is greater than or equal to `min_height` and weight is greater than or equal to `min_weight`, returning a new dictionary with the filtered student information.

