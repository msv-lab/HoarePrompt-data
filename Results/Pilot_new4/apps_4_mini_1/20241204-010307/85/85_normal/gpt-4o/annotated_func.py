#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    max_9s = 0
    while (n + 1) % 10 == 0:
        max_9s += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `max_9s` is the number of trailing nines in the original value of `n`
    pairs = (n + 1) * max_9s
    print(pairs)
#Overall this is what the function does:The function accepts an integer input `n` (where 2 ≤ n ≤ 10^9) and calculates the number of trailing nines in the original value of `n`. It then calculates the value of `(n + 1)` multiplied by the count of trailing nines and prints the result as `pairs`. The function does not have a return statement, so it does not return any value.

