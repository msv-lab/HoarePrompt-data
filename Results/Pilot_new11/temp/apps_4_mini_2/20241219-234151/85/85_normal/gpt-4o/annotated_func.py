#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    max_9s = 0
    while (n + 1) % 10 == 0:
        max_9s += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `max_9s` is equal to the count of trailing 9s in the original value of `n`.
    pairs = (n + 1) * max_9s
    print(pairs)
#Overall this is what the function does:The function accepts an integer input `n` (where 2 ≤ n ≤ 10^9) and calculates the number of trailing 9s in `n`. It then computes a final value by multiplying `(n + 1)` (after the removal of trailing 9s, resulting in `0`) with the count of how many trailing 9s were present initially. The final output produced by the function is always `0` since `n` becomes `0` after the while loop. Therefore, the function effectively counts the trailing 9s in `n`, but it will always print `0` as a result. The function does not handle invalid input cases or provide guidance when `n` does not meet the condition or contains no trailing 9s.

