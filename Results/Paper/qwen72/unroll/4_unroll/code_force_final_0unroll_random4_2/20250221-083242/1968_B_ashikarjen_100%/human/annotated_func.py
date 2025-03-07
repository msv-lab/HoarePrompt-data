#State of the program right berfore the function call: The function should take two parameters, `a` and `b`, where `a` and `b` are binary strings (strings consisting of the characters '0' and '1'). Additionally, the function should be called within a loop that processes `t` test cases, where `t` is an integer such that 1 ≤ t ≤ 10^4. For each test case, `n` and `m` are integers representing the lengths of `a` and `b` respectively, with 1 ≤ n, m ≤ 2 · 10^5. The sum of all `n` values and the sum of all `m` values across all test cases do not exceed 2 · 10^5.
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
        
    #State: `k` is the number of characters in `a` that match a character in `b` in the same order, `j` is the index in `b` where the loop stopped (either because `b[j]` did not match `a[i]` or because `j` reached `m`), `i` is the last index of `a` that was processed, and `n`, `m`, `a`, and `b` remain unchanged.
    print(k)
    #This is printed: k (where k is the number of characters in `a` that match a character in `b` in the same order up to the point where the loop stopped)
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `m` from the input, followed by two binary strings `a` and `b` of lengths `n` and `m` respectively. It then calculates the number of characters in `a` that match a character in `b` in the same order, up to the point where the loop stops (either because `b[j]` does not match `a[i]` or because `j` reaches `m`). The function prints this count `k` and returns nothing. The function is designed to be called within a loop that processes `t` test cases, where `t` is an integer between 1 and 10^4. For each test case, `n`, `m`, `a`, and `b` are read from the input, and the final state of the program after the function concludes is that `k` is printed, and `n`, `m`, `a`, and `b` remain unchanged.

