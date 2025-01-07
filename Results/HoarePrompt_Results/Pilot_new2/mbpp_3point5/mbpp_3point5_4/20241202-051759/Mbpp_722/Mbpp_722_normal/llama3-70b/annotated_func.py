#State of the program right berfore the function call: student_data is a dictionary where keys are student names and values are tuples of floats (student_height, student_weight). min_height and min_weight are floats representing the minimum height and minimum weight respectively.**
def func_1(student_data, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in student_data.
    items() if height >= min_height and weight >= min_weight}
    #The program returns a dictionary where the keys are student names and the values are tuples of floats (student_height, student_weight) for students whose height is greater than or equal to min_height and weight is greater than or equal to min_weight
#Overall this is what the function does:The function func_1 accepts a dictionary student_data with student names as keys and height-weight tuples as values, along with minimum height and weight criteria. It filters the dictionary based on the condition that student height is greater than or equal to min_height and student weight is greater than or equal to min_weight. The filtered dictionary is then returned.

