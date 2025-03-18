#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each of the t test cases, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n over all test cases does not exceed 2 · 10^5, and the sum of all m over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `a` is a binary string of length `n`; `m` is an integer such that 1 ≤ m ≤ 2 · 10^5; `b` is the binary string input by the user; `k` is the number of characters from `a` that were found in `b` in order; `j` is the position in `b` just after the last found character from `a` or `m` if the loop broke early; `i` is equal to `n` if the loop completes all iterations, or the index at which the loop broke.
    print(k)
    #This is printed: k (where k is the number of characters from `a` that were found in `b` in order)
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function reads two integers `n` and `m`, followed by two binary strings `a` and `b`. It calculates the maximum number of characters from `a` that can be found in `b` in the same order and prints this count. The function does not return any value.

