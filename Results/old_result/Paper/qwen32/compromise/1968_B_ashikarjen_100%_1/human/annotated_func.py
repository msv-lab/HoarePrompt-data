#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and m are integers such that 1 <= n, m <= 2 * 10^5. a and b are binary strings of lengths n and m, respectively. The sum of all n values across test cases does not exceed 2 * 10^5, and the sum of all m values across test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` and `m` are integers read from the input such that 1 <= n, m <= 2 * 10^5; `a` is the string read from the input; `b` is the new binary string of length `m` read from the input; `k` is the number of characters from `a` that were found in `b` in the specified order; `j` is the position in `b` after the last match or the position where the search stopped if a match was not found.
    print(k)
    #This is printed: k (where k is the number of characters from `a` that were found in `b` in the specified order)
    return
    #The program does not return any value.
#Overall this is what the function does:The function reads two integers `n` and `m`, followed by two binary strings `a` and `b` of lengths `n` and `m` respectively. It counts the maximum number of characters from string `a` that can be found in string `b` in the specified order and prints this count. The function does not return any value.

