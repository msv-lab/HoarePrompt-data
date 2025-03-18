#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 10^9, `ans` is the count of how many times `n` is a multiple of 10 raised to the power of (the length of the string representation of `n` minus 1).
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (where \( 2 \leq n \leq 10^9 \)) and counts how many integers `i` (ranging from 1 to \( n/2 \)) exist such that the sum of `i` and \( n - i \) is a multiple of \( 10^{(len(i + (n - i)) - 1)} \). It then prints this count. The function does not return any value; it only outputs the result.

