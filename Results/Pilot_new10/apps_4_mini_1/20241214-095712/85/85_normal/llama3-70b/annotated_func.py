#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 10^9, `ans` is the count of valid `i` values satisfying the loop condition for all iterations, `i` iterates from 1 to `n // 2`.
    print(ans)
#Overall this is what the function does:The function accepts no parameters and prompts the user to input an integer `n` (where 2 ≤ n ≤ 10^9). It then calculates and prints the count of integers `i` (from 1 to n//2) such that the sum of `i` and `n-i` is divisible by the largest power of 10 less than or equal to that sum. The function does not return any value.

