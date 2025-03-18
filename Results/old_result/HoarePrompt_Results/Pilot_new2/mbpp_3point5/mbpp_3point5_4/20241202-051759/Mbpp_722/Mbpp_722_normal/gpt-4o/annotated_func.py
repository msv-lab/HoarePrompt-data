#State of the program right berfore the function call: student_dict is a dictionary where keys are strings representing student names and values are tuples of two floats representing student height and weight, min_height and min_weight are floats representing the minimum height and minimum weight respectively.**
def func_1(student_dict, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in student_dict.
    items() if height >= min_height and weight >= min_weight}
    #The program returns a dictionary where keys are student names and values are tuples of height and weight for students whose height is greater than or equal to min_height and weight is greater than or equal to min_weight
#Overall this is what the function does:The function accepts a dictionary of student data, a minimum height, and a minimum weight. It then filters the dictionary to return a new dictionary containing only the students whose height is greater than or equal to min_height and weight is greater than or equal to min_weight. If any student data is missing height or weight information, it will not be included in the filtered dictionary.

