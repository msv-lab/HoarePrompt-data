#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2 ⋅ 10^5. a is a binary string of length n, and b is a binary string of length m. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5, and the sum of all m values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: `j` is `m`, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `a` is a string representing the input integer n, `b` is the input string from the user, `k` is the number of times `a[i]` matches any character in `b` up to index `m-1`.
    print(k)
    #This is printed: k (where k is the number of times a character in a matches any character in b up to index m-1)
    return
    #The program does not return any value since there is no return statement in the provided code snippet.
#Overall this is what the function does:The function processes two binary strings, `a` and `b`, of lengths `n` and `m` respectively, across multiple test cases. It counts and outputs the number of times any character in string `a` matches any character in string `b` up to the last character of `b`. The function does not return any value.

