#State of the program right berfore the function call: Input consists of up to 50 lines, each containing a student ID (an integer between 1 and 2000), weight (a real number between 1 and 200), and height (a real number between 1.0 and 2.0), formatted as "si, wi, hi".
def func():
    for line in stdin:
        number, weight, height = line.split(',')
        
        if 25.0 <= float(weight) / float(height) ** 2:
            print(number)
        
    #State of the program after the  for loop has been executed: `number`, `weight`, `height` are assigned values from the input for each line that meets the condition of having a BMI of 25.0 or greater. If no input meets this condition, the variables will retain the values from the last line read or remain unassigned if the input was empty.
#Overall this is what the function does:The function processes input consisting of up to 50 lines, each containing a student ID (an integer between 1 and 2000), weight (a real number between 1 and 200), and height (a real number between 1.0 and 2.0). It calculates the Body Mass Index (BMI) for each entry and prints the student ID for those entries where the BMI is 25.0 or greater. If the input is empty or no entries meet the BMI condition, nothing is printed. The function does not return any value.

