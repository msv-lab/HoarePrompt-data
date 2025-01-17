#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n, m, and k are integers such that 1 ≤ m, k ≤ n ≤ 50.
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
#Overall this is what the function does:The function `func_1` accepts three parameters `n`, `m`, and `k`, which are integers constrained by 1 ≤ m, k ≤ n ≤ 50. It returns either 'YES' or 'NO' based on the following conditions:
- If `m == k` or `k > n`, the function returns 'NO'.
- If `m > k`, the function returns 'YES'.
- Otherwise, the function returns 'NO'.

The final state of the program after the function concludes is that it has returned either 'YES' or 'NO' based on the evaluated conditions. There are no additional side effects or changes to external states.

