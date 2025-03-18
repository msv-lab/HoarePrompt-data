#State of the program right berfore the function call: t is an integer where 1 <= t <= 2 * 10^4, n is an integer where 1 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    for tc in range(int(input())):
        N = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = defaultdict(int)
        
        for i in range(N):
            cnt[a[i]] += 1
        
        t = 0
        
        for i in range(N):
            if cnt[i] == 1:
                t += 1
            if t >= 2 or cnt[i] == 0:
                print(i)
                break
        
    #State: t is an integer where 1 <= t <= 2 * 10^4, n is an integer where 1 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 * 10^5. The variable `tc` is incremented by the number of test cases executed, and the variable `t` is reset to 0 for each test case. The loop prints the first index `i` where `cnt[i] == 1` or `cnt[i] == 0` and breaks out of the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `N` and a list `a` of `N` integers. For each test case, it counts the occurrences of each integer in `a`. It then prints the first index `i` where the integer `i` appears exactly once in `a` or where `i` does not appear at all, and breaks out of the loop. If no such index is found, the function does not print anything for that test case. The function does not return any value.

