#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `ans` is the count of times the sum `n` satisfies the condition, `n` is an integer such that 2 ≤ n ≤ 10^9.
    print(ans)
#Overall this is what the function does:The function accepts an integer input `n` (where 2 ≤ n ≤ 10^9) from the user. It calculates how many pairs of integers `(i, n - i)` exist such that `i` is in the range from 1 to `n // 2`, and the sum of these pairs is divisible by the largest power of ten less than or equal to that sum. The result is printed as the count of such pairs.

