#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n, with each integer from 1 to n appearing at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The variable `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, and `a` is a list of n integers where 1 ≤ a_i ≤ n, with each integer from 1 to n appearing at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5. The `input` variable is the next line of input after all iterations of the loop have completed. The `cnt` list is reset to a list of zeros of length n + 1 after each iteration, and `ans` is calculated and printed for each iteration, but its final value is not retained between iterations.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case involves a list of integers `a` of length `n`. For each test case, the function calculates the number of integers in `a` that appear more than once and prints this count. The function does not return any value but prints the result for each test case. After processing all test cases, the function concludes, and the state of the program is such that the input has been fully read, and the results for all test cases have been printed.

