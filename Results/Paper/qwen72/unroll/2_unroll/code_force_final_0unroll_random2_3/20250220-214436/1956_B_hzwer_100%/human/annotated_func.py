#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n, with each integer from 1 to n appearing at most twice. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n, with each integer from 1 to n appearing at most twice. The sum of n over all test cases does not exceed 2 · 10^5. The `input` function is now set to read from standard input using `sys.stdin.readline`. The loop has processed all test cases, and for each test case, it has printed the number of integers in the list `a` that appear more than once.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it reads an integer `n` and a list `a` of `n` integers. It then calculates and prints the number of integers in `a` that appear more than once. The function does not return any value; it only prints the results to the standard output. After the function concludes, the state of the program is such that `t` test cases have been processed, and the results for each test case have been printed. The input variables `t`, `n`, and `a` are not modified by the function.

