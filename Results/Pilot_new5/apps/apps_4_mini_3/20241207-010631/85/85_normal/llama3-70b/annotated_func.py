#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 10^9, `ans` is the count of pairs (i, n-i) where the condition is satisfied, `i` is n // 2 after the loop completes.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (2 ≤ n ≤ 10^9) and counts the number of pairs `(i, n-i)` for `1 ≤ i ≤ n/2` such that the sum `i + (n - i)` is divisible by the highest power of 10 that is less than or equal to that sum. It then prints the count of such pairs. The function does not return any value; it simply outputs the result.

