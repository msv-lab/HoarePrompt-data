#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    max_9s = 0
    while (n + 1) % 10 == 0:
        max_9s += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `max_9s` is the count of how many times `n` originally ended in the digit 9
    pairs = (n + 1) * max_9s
    print(pairs)
#Overall this is what the function does:The function accepts an integer input `n` (where 2 ≤ n ≤ 10^9) and counts how many times `n` ends with the digit 9, by checking whether (n + 1) is divisible by 10. The function then calculates the product of (n + 1) and the count of trailing 9s and prints the result. If `n` initially ends in 0, the function will not count any trailing 9s and will produce an output based on the value of `(n + 1) * max_9s`, which will be `n + 1`. The output will vary depending on how many times `n` had the digit 9 at the end.

