#State of the program right berfore the function call: The function takes no input parameters, but based on the problem description, it is expected to process multiple test cases. Each test case includes an integer n (1 ≤ n ≤ 3 · 10^5) representing the length of the array, and an array a of length n where each element a_i (1 ≤ a_i ≤ n) is a positive integer. The array a is guaranteed to be beautiful, and the sum of n over all test cases does not exceed 3 · 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().strip().split()))
        
        tmp = a[0]
        
        cnt = 0
        
        ans = n
        
        for i in range(n):
            if a[i] == tmp:
                cnt += 1
            else:
                ans = min(ans, cnt)
                cnt = 0
        
        ans = min(ans, cnt)
        
        if n == 1 or ans == n:
            print(-1)
        else:
            print(ans)
        
    #State: The loop has processed all `t` test cases. For each test case, the output is either `-1` if the array length `n` is 1 or if all elements in the array are the same, or the minimum count of consecutive elements that are the same, excluding the entire array length. The variables `t`, `n`, and `a` are no longer relevant after the loop completes.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing an integer `n` and an array `a` of length `n`. For each test case, it calculates the minimum count of consecutive elements that are the same in the array `a`, excluding the entire array length if all elements are the same. If the array length `n` is 1 or if all elements in the array are the same, it prints `-1`. Otherwise, it prints the minimum count of consecutive identical elements. After processing all test cases, the function completes and the variables `t`, `n`, and `a` are no longer relevant.

