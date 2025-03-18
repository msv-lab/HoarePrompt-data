#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n, and each integer from 1 through n appears in the list a at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = [0] * (n + 1)
        
        for x in a:
            cnt[x] += 1
        
        ans = 0
        
        for x in cnt:
            ans += max(0, x - 1)
        
        print(ans)
        
    #State: The loop has printed the result `ans` for each of the `t` test cases, where `ans` is the sum of `max(0, x - 1)` for each element `x` in the count array `cnt` that tracks the occurrences of integers in the list `a` for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. It calculates and prints the total number of integers that appear more than once in the list `a` for each test case.

