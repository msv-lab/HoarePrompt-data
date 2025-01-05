#State of the program right berfore the function call: Each student's data is given in the format "si, wi, hi" where si is an integer representing the student ID number (1 ≤ si ≤ 2,000), wi is a real number representing the weight of the student (1 ≤ wi ≤ 200), and hi is a real number representing the height of the student (1.0 ≤ hi ≤ 2.0). The number of students does not exceed 50.**
def func():
    for line in stdin:
        number, weight, height = line.split(',')
        
        if 25.0 <= float(weight) / float(height) ** 2:
            print(number)
        
    #State of the program after the  for loop has been executed: All `number` values where 25.0 <= float(weight) / float(height) hold true will be printed.
#Overall this is what the function does:The function `func()` processes the data of students provided in the format "si, wi, hi", where si is the student ID number, wi is the weight of the student, and hi is the height of the student. It reads the input data from standard input and checks if the weight to height ratio of each student is greater than or equal to 25.0. If this condition is met, it prints the student's ID number. The function does not accept any parameters and handles the data for each student according to specified constraints.

