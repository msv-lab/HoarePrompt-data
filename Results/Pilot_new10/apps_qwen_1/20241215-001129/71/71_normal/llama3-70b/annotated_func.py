#State of the program right berfore the function call: The function takes no input parameters but relies on input from stdin in the form of two space-separated integers n and k, where 0 ≤ n ≤ 2 000 000 000 and 1 ≤ k ≤ 9, and guarantees that the answer exists.
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: 'n' is reduced to an integer between 0 and 2,000,000 inclusive and still not divisible by \(10^k\), 'w' is the number of times the loop executed.
    print(w)
#Overall this is what the function does:The function reads two integers `n` and `k` from standard input, reduces `n` to an integer between 0 and 2,000,000 inclusive, and counts the number of times `n` is divided by 10 until it is not divisible by \(10^k\). It then prints the count of such divisions.

