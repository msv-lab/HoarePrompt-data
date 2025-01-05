#State of the program right berfore the function call: There is no specific precondition for this problem as the input values are simply 10 integers representing the score of each question.
def func():
    k = 0
    for i in range(10):
        k = k + int(input())
        
    #State of the program after the  for loop has been executed: `k` is the sum of all input integers, `i` is 9
    print(k)
#Overall this is what the function does:The function calculates the total score by summing up the scores of 10 questions inputted by the user and prints the total score as an integer.

