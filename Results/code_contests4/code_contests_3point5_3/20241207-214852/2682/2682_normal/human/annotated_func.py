#State of the program right berfore the function call: Each input line contains a student ID (si), weight (wi), and height (hi) where 1 ≤ si ≤ 2,000, 1 ≤ wi ≤ 200, and 1.0 ≤ hi ≤ 2.0. The number of students is at most 50.**
def func():
    for line in stdin:
        number, weight, height = line.split(',')
        
        if 25.0 <= float(weight) / float(height) ** 2:
            print(number)
        
    #State of the program after the  for loop has been executed: After the loop executes, the program will print the `number` of the students whose weight divided by the square of their height is greater than or equal to 25.0.
#Overall this is what the function does:The function `func` reads input data for multiple students, each identified by a student ID, weight, and height. It then calculates the Body Mass Index (BMI) for each student based on the weight and height provided. If the BMI is greater than or equal to 25.0, it prints the student ID. The function does not accept any parameters. It handles at most 50 students and processes their data to identify those with a high BMI.

