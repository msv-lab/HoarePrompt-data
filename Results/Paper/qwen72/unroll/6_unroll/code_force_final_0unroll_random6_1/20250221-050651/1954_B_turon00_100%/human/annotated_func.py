#State of the program right berfore the function call: The function `func` is expected to take input through standard input and output through standard output, as it does not have any parameters defined. The input consists of multiple test cases, where the first line contains a single integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case starts with a single integer n (1 ≤ n ≤ 3 · 10^5) followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n), forming a beautiful array. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop completes its execution, and for each test case, it prints the minimum count of consecutive elements that are the same as the first element of the array, or -1 if the array has only one element or all elements are the same. The variables `t`, `n`, `a`, `tmp`, `cnt`, and `ans` are no longer in use after the loop finishes.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input. Each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates the minimum count of consecutive elements that are the same as the first element of the array. If the array has only one element or all elements are the same, it prints `-1`. Otherwise, it prints the minimum count. After processing all test cases, the function completes, and the variables used within the function are no longer in use.

