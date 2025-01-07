#State of the program right berfore the function call: student_dict is a dictionary where keys are strings representing student names and values are tuples of two floats (student_height, student_weight). min_height and min_weight are floats representing the minimum height and minimum weight respectively.**
def func_1(student_dict, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in student_dict.
    items() if height >= min_height and weight >= min_weight}
    #The program returns a dictionary where each key-value pair consists of student names and their corresponding heights and weights, but only for students whose height is greater than or equal to min_height and weight is greater than or equal to min_weight.
#Overall this is what the function does:The function `func_1` accepts three parameters: `student_dict`, `min_height`, and `min_weight`. The parameter `student_dict` is a dictionary where keys are strings representing student names and values are tuples of two floats (student_height, student_weight). The function filters the student information based on the minimum height and weight provided, returning a dictionary with only the students whose height is greater than or equal to `min_height` and weight is greater than or equal to `min_weight`.

