#State of the program right berfore the function call: student_dict is a dictionary where keys are strings (student names) and values are tuples of two floats (student_height, student_weight). min_height and min_weight are floats representing the minimum height and minimum weight respectively.**
def func_1(student_dict, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in student_dict.
    items() if height >= min_height and weight >= min_weight}
    #The program returns a dictionary containing student names along with their corresponding height and weight tuples, only including students whose height is greater than or equal to min_height and weight is greater than or equal to min_weight
#Overall this is what the function does:The function func_1 accepts a dictionary named student_dict with student names as keys and tuples of height and weight as values, along with minimum height and minimum weight values. It then filters the student_dict based on the condition that only students with height greater than or equal to min_height and weight greater than or equal to min_weight are included in the returned dictionary.

