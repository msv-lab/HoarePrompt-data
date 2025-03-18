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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is a string obtained from the first space-separated integer input, `m` is an integer obtained from the second space-separated integer input, `b` is a string obtained from the next input, `k` is an integer representing the number of times `a[i]` matched `b[j]` before `j` reached `m` or the end of the loop, `j` is an integer representing the position in string `b` where the loop last attempted to find a match for `a[i]`.
    print(k)
    #This is printed: k (the number of times `a[i]` matched `b[j]` before `j` reached `m` or the end of the loop)
    return
    #The program returns None
#Overall this is what the function does:The function reads two integers \( n \) and \( m \), followed by two binary strings \( a \) and \( b \). It then compares each character of \( a \) with \( b \) up to the length of \( b \), counting the number of matches. Finally, it prints the count of matches and returns None.

