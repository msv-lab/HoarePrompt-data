#State of the program right berfore the function call: The function `func` is expected to take input parameters, but the function definition provided does not include any parameters. Based on the problem description, the function should take a list of integers `a` as input, where `a` is a beautiful array, and an integer `n` representing the length of the array `a` (1 ≤ n ≤ 3 · 10^5). Additionally, the function should handle multiple test cases, which implies that it might need to take an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases, and for each test case, the array `a` and its length `n`. However, the function definition should be corrected to include these parameters.
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
        
    #State: The loop will execute `t` times, each time processing a list of integers `a` of length `n`. For each test case, the loop will print either `-1` if `n` is 1 or if all elements in `a` are the same, or the minimum count of consecutive elements that are the same as the first element in `a`. After all iterations, the variables `t`, `n`, `a`, `tmp`, `cnt`, and `ans` will have been updated according to the logic of the loop, but their final values will depend on the input provided during the execution.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` representing the length of a list of integers `a`. It then processes the list `a` to find the minimum count of consecutive elements that are the same as the first element in `a`. If the length `n` is 1 or all elements in `a` are the same, it prints `-1`. Otherwise, it prints the minimum count found. After processing all test cases, the function terminates, and the variables `t`, `n`, `a`, `tmp`, `cnt`, and `ans` will have been updated according to the input and the logic of the function.

