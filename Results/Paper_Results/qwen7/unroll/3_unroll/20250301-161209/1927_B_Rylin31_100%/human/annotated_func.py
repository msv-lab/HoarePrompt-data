#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; a is a list of n non-negative integers such that 0 ≤ a_i < n, representing the trace of the string.
def func():
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; a is a list of n non-negative integers such that 0 ≤ a_i < n, representing the trace of the string; after executing the loop, ans is a string constructed by iterating through the list 'a' and appending characters based on the current value of s[j] plus 97, then incrementing s[j] by 1 for each iteration.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n` and a list `a` of length `n`. It then constructs a string `ans` by iterating through the list `a` and appending characters based on the current value of `s[j]` (initialized to 0 for each index `j`) plus 97, then increments `s[j]` by 1 for each iteration. Finally, it prints the constructed string `ans` for each test case.

