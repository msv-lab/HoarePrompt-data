#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5, and similarly, the sum of all m values does not exceed 2 ⋅ 10^5.
def func_1():
    n, m = map(int, input().split())
    a = input()
    b = input()
    k = 0
    j = 0
    for i in range(n):
        while j < m and b[j] != a[i]:
            j += 1
        
        if j < m:
            k += 1
            j += 1
        else:
            break
        
    #State: `j` is greater than or equal to `m + n`, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is a positive integer, `b` is a non-empty string, `k` is either 0 or a value between 0 and `n`, inclusive, `i` is `m + n - 1`, and for all `p` where `m <= p < j`, `b[p]` is not equal to `a[i]` if `k` is greater than 0.
    print(k)
    #This is printed: k
    return
    #The program returns None
#Overall this is what the function does:The function reads two binary strings `a` and `b` along with their lengths `n` and `m` respectively. It then counts the number of positions where the characters of `a` match the characters of `b`. If a match is found, the index in `b` is incremented. After processing all characters in `a`, the function prints the count of matches and returns None.

