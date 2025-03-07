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
        
    #State: Output State: `j` is equal to `m`, `t` remains unchanged, `n` remains unchanged, `m` remains unchanged, `a` remains unchanged, `b` remains unchanged, `k` is equal to the number of characters in `a` that are present in `b` up to index `m-1`.
    print(k)
    #This is printed: k (the number of characters in `a` that are present in `b` up to index `m-1`)
#Overall this is what the function does:The function processes multiple test cases, each consisting of two binary strings `a` and `b` of lengths `n` and `m` respectively. For each test case, it counts and prints the number of characters in `a` that also appear in `b` up to index `m-1`. After processing all test cases, the function outputs the count for each test case.

