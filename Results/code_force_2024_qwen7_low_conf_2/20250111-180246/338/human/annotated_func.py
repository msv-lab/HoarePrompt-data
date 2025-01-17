#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n, m, and k are positive integers satisfying 1 ≤ m, k ≤ n ≤ 50.
def func_1(n, m, k):
    if (m == k or k > n) :
        return 'NO'
        #The program returns 'NO'
    else :
        if (m > k) :
            return 'YES'
            #The program returns 'YES'
        else :
            return 'NO'
            #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts three positive integers `n`, `m`, and `k` and returns either 'YES' or 'NO'. Based on the following conditions:
- If `m == k` or `k > n`, the function returns 'NO'.
- If `m > k`, the function returns 'YES'.
- Otherwise, the function returns 'NO'.

The function covers all potential cases:
- When `m == k` or `k > n`, the function returns 'NO'.
- When `m > k`, the function returns 'YES'.
- In any other case, the function also returns 'NO'.

The final state of the program after it concludes is that it returns either 'YES' or 'NO' based on the given conditions.

