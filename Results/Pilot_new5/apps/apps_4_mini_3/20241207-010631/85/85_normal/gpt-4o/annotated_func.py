#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    max_9s = 0
    while (n + 1) % 10 == 0:
        max_9s += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `max_9s` is the count of trailing 9s in the initial value of `n`
    pairs = (n + 1) * max_9s
    print(pairs)
#Overall this is what the function does:The function accepts an integer input `n` (with 2 ≤ n ≤ 10^9) and calculates the number of trailing 9s in its decimal representation. It then calculates the product of `(n + 1)` and the count of trailing 9s, printing this result. The function does not return any value.

