#State of the program right berfore the function call: The function `func` is expected to process multiple test cases. Each test case includes an integer `n` (1 ≤ n ≤ 3 · 10^5) representing the length of the array, and an array `a` of length `n` where each element `a_i` (1 ≤ a_i ≤ n) is a positive integer. The array `a` is guaranteed to be beautiful, meaning it is possible to make all elements the same by performing the specified operation. The sum of `n` over all test cases does not exceed 3 · 10^5. The function should return the minimum number of elements to remove to make the array non-beautiful, or -1 if it is impossible.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        aa = set(a)
        
        if len(aa) == 1:
            print(-1)
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        print(ans)
        
    #State: After all iterations of the loop, the variable `t` will be 0 (since the loop iterates `t` times), and the variables `n` and `a` will hold the values of the last test case processed. The variable `tmp` will hold the first element of the last test case's array `a`. The variable `aa` will be a set containing the unique elements of the last test case's array `a`. The variable `cnt` will be 0, and the variable `ans` will hold the minimum number of elements to remove to make the last test case's array non-beautiful, or -1 if it is impossible.
#Overall this is what the function does:The function `func` processes multiple test cases. Each test case consists of an integer `n` and an array `a` of length `n`. The function prints the minimum number of elements that need to be removed from the array to make it non-beautiful, where a beautiful array is one where all elements can be made the same by performing a specified operation. If it is impossible to make the array non-beautiful, the function prints -1. After processing all test cases, the function does not return any value, but the variables `t`, `n`, `a`, `tmp`, `aa`, `cnt`, and `ans` will hold the state of the last test case processed.

