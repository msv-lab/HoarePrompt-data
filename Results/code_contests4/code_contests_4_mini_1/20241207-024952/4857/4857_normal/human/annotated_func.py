#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10,000.
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
        
    #State of the program after the loop has been executed: `x` is less than the last `i + k`, `i` is the last triangular number reached, `k` is the next incremented value, `c` is the count of loop iterations, `n` is an integer such that 1 ≤ `n` ≤ 10,000
    print(c)
#Overall this is what the function does:The function accepts an integer input from the user, which must be between 1 and 10,000. It calculates how many triangular numbers (1, 3, 6, 10, etc.) can be subtracted from the input number until the remaining value becomes negative. The function then prints the count of these iterations. The function does not return a value; it only outputs the count.

