#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^4.**
def func():
    x = int(input())
    i = 0
    k = 1
    c = 0
    while x - (i + k) >= 0:
        i = i + k
        
        x = x - i
        
        c = c + 1
        
        k = k + 1
        
    #State of the program after the loop has been executed: `i` is the sum of all numbers from 1 to the initial value of `k` minus 1, `k` is the initial value of `k` plus 1, `c` is the number of times the loop executed, `x` is less than the final value of `i`
    print(c)
#Overall this is what the function does:The function `func` reads an integer input `x`, calculates the sum of integers from 1 to a certain point based on `x`, and prints the number of iterations it took to reach a point where subtracting the sum from `x` results in a non-positive value. The function does not have return values and operates without taking any parameters.

