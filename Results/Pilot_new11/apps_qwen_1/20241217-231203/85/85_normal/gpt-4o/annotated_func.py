#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    max_9s = 0
    while (n + 1) % 10 == 0:
        max_9s += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is the integer value of `n` with all trailing 9s removed, `max_9s` is the count of trailing 9s that were removed from the original value of `n`.
    pairs = (n + 1) * max_9s
    print(pairs)
#Overall this is what the function does:The function reads an integer \( n \) from the user where \( 2 \leq n \leq 10^9 \). It then counts the number of trailing 9s in \( n \), removes those trailing 9s, and calculates a value based on the remaining part of \( n \) and the count of trailing 9s. Specifically, it computes \( (n + 1) \times \text{count of trailing 9s} \) and prints the result. If \( n \) does not have any trailing 9s, the count will be 0, and the result will be \( n + 1 \).

