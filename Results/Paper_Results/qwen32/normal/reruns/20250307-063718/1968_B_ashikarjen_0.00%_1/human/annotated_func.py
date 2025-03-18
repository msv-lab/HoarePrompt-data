#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there are three lines: two integers n and m (1 ≤ n, m ≤ 2 · 10^5) representing the lengths of binary strings a and b, respectively; a binary string a of length n; and a binary string b of length m. It is guaranteed that the sum of all n and m over all test cases does not exceed 2 · 10^5.
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
        
    #State: - `n` remains unchanged.
    #- `m` remains unchanged.
    #- `t` remains unchanged.
    #- `a` remains unchanged.
    #- `b` remains unchanged.
    #- `k` is the number of characters in `a` that were found in `b` in the same order.
    #- `j` is the index in `b` where the search stopped.
    #
    #Output State:
    print(k)
    #This is printed: k (where k is the number of characters in `a` that were found in `b` in the same order)
#Overall this is what the function does:The function processes a series of test cases, each consisting of two binary strings `a` and `b`. For each test case, it calculates and prints the number of characters in `a` that can be found in `b` in the same order. The function does not modify the input strings or the number of test cases.

