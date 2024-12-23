#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(2 \leq n \leq 10^9\), `ans` is the count of `i` in the range \(1 \leq i \leq n // 2 + 1\) for which \((i + (n - i)) \mod 10^{(\text{len}(str(i + (n - i))) - 1)} == 0\).
    print(ans)
#Overall this is what the function does:The function reads an integer \( n \) from the user where \( 2 \leq n \leq 10^9 \). It then iterates through the range from 1 to \( \frac{n}{2} + 1 \) (inclusive) and counts the number of integers \( i \) in this range for which the sum \( i + (n - i) \) is divisible by \( 10 \) raised to the power of one less than the length of the string representation of \( i + (n - i) \). Finally, it prints the count of such integers. The function does not handle any edge cases explicitly mentioned in the annotations; however, it implicitly handles the case where \( n \) is even or odd. If \( n \) is even, \( \frac{n}{2} + 1 \) will be an integer, and if \( n \) is odd, \( \frac{n}{2} + 1 \) will be a half-integer rounded up.

