#State of the program right berfore the function call: student_data is a dictionary where keys are student names and values are tuples of floats (student_height, student_weight). min_height and min_weight are floats representing the minimal height and weight respectively.**
def func_1(student_data, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in student_data.
    items() if height >= min_height and weight >= min_weight}
    #The program returns a dictionary containing only the student names and corresponding tuples of height and weight from the student_data dictionary where both the height is greater than or equal to min_height and weight is greater than or equal to min_weight.
#Overall this is what the function does:The function func_1 accepts a dictionary `student_data`, along with `min_height` and `min_weight` floats. It then filters the student data based on the condition that both the height and weight of the students are greater than or equal to `min_height` and `min_weight` respectively. The function returns a dictionary containing only the student names and corresponding tuples of height and weight that meet the specified criteria.

