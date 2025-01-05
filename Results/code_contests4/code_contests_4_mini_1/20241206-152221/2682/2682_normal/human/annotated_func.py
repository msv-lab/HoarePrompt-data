#State of the program right berfore the function call: Each line of input contains a student ID (si) as an integer (1 ≤ si ≤ 2000), weight (wi) as a real number (1 ≤ wi ≤ 200), and height (hi) as a real number (1.0 ≤ hi ≤ 2.0). The number of students does not exceed 50.
def func():
    for line in stdin:
        number, weight, height = line.split(',')
        
        if 25.0 <= float(weight) / float(height) ** 2:
            print(number)
        
    #State of the program after the  for loop has been executed: `number`, `weight`, and `height` are assigned values from input for each student, and the student ID (`number`) is printed for all students whose BMI (calculated as `weight` divided by the square of `height`) is greater than or equal to 25.0. If no students meet this criterion, no output is produced.
#Overall this is what the function does:The function processes input lines containing student IDs, weights, and heights, calculates the Body Mass Index (BMI) for each student, and prints the student ID for those whose BMI is greater than or equal to 25.0. If no students meet this criterion, there will be no output. The function does not return any values or accept parameters directly.

