#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers such that 1 ≤ a_i ≤ n, where each integer from 1 to n appears at most 2 times in the list a. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop reads a number of test cases from the input, and for each test case, it reads an integer `n` and a list of `n` integers `a`. It then counts the occurrences of each integer in `a` and calculates the number of integers that appear more than once. This count is printed for each test case. After all iterations of the loop, the variables `input`, `n`, `a`, `cnt`, and `ans` will have been updated and used for each test case, but their final values will be the ones from the last test case processed. The loop itself does not modify the initial state outside of its scope.
#Overall this is what the function does:The function reads a series of test cases from the standard input. For each test case, it reads an integer `n` and a list of `n` integers `a`. It then counts the occurrences of each integer in `a` and calculates the number of integers that appear more than once. This count is printed for each test case. After processing all test cases, the function has no return value, but the standard output will contain the results for each test case, and the variables `input`, `n`, `a`, `cnt`, and `ans` will retain the values from the last test case processed.

