#State of the program right berfore the function call: Each student ID (si) is an integer between 1 and 2000, weight (wi) is a real number between 1 and 200, and height (hi) is a real number between 1.0 and 2.0. The number of students does not exceed 50.**
def func():
    for line in stdin:
        number, weight, height = line.split(',')
        
        if 25.0 <= float(weight) / float(height) ** 2:
            print(number)
        
    #State of the program after the  for loop has been executed: The loop will iterate over each line from the input and check if the weight divided by the square of the height is greater than or equal to 25. If true, it will print the student ID. Therefore, after all iterations of the loop have finished, the output will be the student IDs that meet the condition 25.0 <= weight / height^2.
#Overall this is what the function does:The function `func` reads input lines containing student IDs, weights, and heights. It calculates the Body Mass Index (BMI) for each student using the formula BMI = weight / (height * height) and prints the student ID if their BMI is greater than or equal to 25.0. The function categorizes students into Underweight, Normal weight, Overweight, or Obese based on their BMI. However, the function does not categorize students into specific BMI categories as mentioned in the annotations. It solely prints the student ID if their BMI is 25.0 or higher.

