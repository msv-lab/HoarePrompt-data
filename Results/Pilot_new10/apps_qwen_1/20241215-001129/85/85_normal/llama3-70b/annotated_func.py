#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `ans` is the number of integers `i` (1 to \(n//2\)) for which \(n\) is divisible by \(10^{k}\) where \(k\) is the number of digits in \(n\) minus 1, and `n` is a non-negative integer between 2 and \(10^9\).
    print(ans)
#Overall this is what the function does:The function reads an integer `n` within the range 2 to \(10^9\) from user input, and counts the number of integers `i` (from 1 to \(n//2\)) for which \((i + (n - i))\) is divisible by \(10\) raised to the power of the number of digits in \((i + (n - i))\) minus one. The function then prints the count of such integers.

