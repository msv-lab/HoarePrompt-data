#State of the program right berfore the function call: The function reads 10 integers from input, each representing the score of a problem, where each integer si is in the range 0 ≤ si ≤ 100.
def func():
    k = 0
    for i in range(10):
        k = k + int(input())
        
    #State of the program after the  for loop has been executed: `k` is the sum of the 10 integers read from input, `i` is 10.
    print(k)
#Overall this is what the function does:The function reads 10 integers from user input, each representing a score in the range 0 to 100, calculates their sum, and prints the total sum. It does not return any value.

