#State of the program right berfore the function call: The function reads 10 integers from input, each representing the score of a problem, where each integer si satisfies 0 ≤ si ≤ 100.
def func():
    k = 0
    for i in range(10):
        k = k + int(input())
        
    #State of the program after the  for loop has been executed: `k` is the sum of the 10 integer inputs, `i` is 9.
    print(k)
#Overall this is what the function does:The function reads 10 integers from input, each representing a score that satisfies 0 ≤ si ≤ 100, and calculates their sum, which it then prints. There is no return value, and the function does not handle cases where the input may not be an integer or is out of the specified range.

