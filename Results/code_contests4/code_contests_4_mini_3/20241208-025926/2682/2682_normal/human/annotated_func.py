#State of the program right berfore the function call: The input consists of up to 50 lines, each containing a student ID (an integer between 1 and 2000), weight (a real number between 1 and 200), and height (a real number between 1.0 and 2.0), separated by commas.
def func():
    for line in stdin:
        number, weight, height = line.split(',')
        
        if 25.0 <= float(weight) / float(height) ** 2:
            print(number)
        
    #State of the program after the  for loop has been executed: `number` is a string representation of student ID, `weight` is a string representation of weight, and `height` is a string representation of height for each student. If the value of weight divided by the square of height is greater than or equal to 25.0 for any student, the corresponding student ID `number` is printed. If no student meets the condition, no IDs are printed.
#Overall this is what the function does:The function processes input lines containing student IDs, weights, and heights, and prints the student IDs for which the Body Mass Index (BMI) calculated as weight divided by the square of height is greater than or equal to 25.0. The function does not accept parameters or return any values. It does not handle cases where the input format may be incorrect or where the weight or height might not be convertible to float, potentially leading to runtime errors.

