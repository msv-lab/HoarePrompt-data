#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    max_9s = 0
    while (n + 1) % 10 == 0:
        max_9s += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `max_9s` is equal to the number of trailing 9s in the original value of `n` (if `n` had at least one trailing 9). If `n` had no trailing 9s, `max_9s` is 0.
    pairs = (n + 1) * max_9s
    print(pairs)
#Overall this is what the function does:The function accepts an integer input `n`, where `2 ≤ n ≤ 10^9`, and calculates the number of trailing 9s in `n`. It returns the product of `(n + 1)` and the count of trailing 9s. If `n` has no trailing 9s, it will return the value of `n + 1` multiplied by 0, which is 0. The function does not return a value but prints the result.

