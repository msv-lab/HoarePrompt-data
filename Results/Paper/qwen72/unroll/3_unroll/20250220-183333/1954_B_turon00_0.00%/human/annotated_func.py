#State of the program right berfore the function call: The function is expected to handle multiple test cases. For each test case, the input is a single integer n (1 ≤ n ≤ 3 · 10^5) representing the length of the array, followed by an array a of n integers (1 ≤ a_i ≤ n) that is guaranteed to be beautiful. The total number of test cases t is a positive integer (1 ≤ t ≤ 10^4), and the sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop iterates through each test case, reads the integer `n` and the array `a` for each test case, and prints the minimum length of consecutive elements that are the same as the first element in the array `a`. If all elements in the array `a` are the same, it prints -1. The variables `t`, `n`, `a`, `tmp`, `aa`, `cnt`, and `ans` are updated and used within the loop, but their final values after the loop are not relevant to the next test case, as they are reset for each iteration.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case consists of an integer `n` and an array `a` of `n` integers. For each test case, it prints the minimum length of consecutive elements in the array `a` that are the same as the first element. If all elements in the array `a` are the same, it prints -1. The function does not return any values; it only prints the results for each test case. After processing all test cases, the function concludes, and the program state is reset for the next call.

