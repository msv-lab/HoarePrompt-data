#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 1000.
def func():
    n = int(raw_input())
    for i in range(n / 2):
        if gcd(n - i, i) == 1:
            print(str(i) + ' ' + str(n - i))
        
    #State of the program after the  for loop has been executed: `i` is the largest integer in the range `[0, n/2]` for which `gcd(n - i, i) == 1`, `n - i` is the corresponding value, and `n` is an integer within the range 3 ≤ n ≤ 1000. If no such `i` exists, `i` is 0 and `n - i` is `n`.
#Overall this is what the function does:The function takes an integer \( n \) (where \( 3 \leq n \leq 1000 \)) as input, iterates over the range from 0 to \( n/2 \), and prints pairs of integers \((i, n-i)\) where \( i \) and \( n-i \) are coprime (i.e., their greatest common divisor is 1). After the loop, the function ends without returning any value. If no pair \((i, n-i)\) satisfying the condition is found, the loop simply completes without printing anything.

