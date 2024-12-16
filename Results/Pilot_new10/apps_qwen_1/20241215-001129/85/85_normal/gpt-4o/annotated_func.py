#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    max_9s = 0
    while (n + 1) % 10 == 0:
        max_9s += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is the integer input from the user, with no trailing 9s (i.e., `n` is not divisible by 10), `max_9s` is the count of consecutive trailing 9s in the original value of `n`
    pairs = (n + 1) * max_9s
    print(pairs)
#Overall this is what the function does:The function takes an integer `n` (where \(2 \leq n \leq 10^9\)), counts the number of trailing 9s in `n`, and prints the result of \((n + 1) * max_9s\).

