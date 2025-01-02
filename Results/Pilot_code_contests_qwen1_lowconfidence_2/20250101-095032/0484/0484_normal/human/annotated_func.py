#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 100, and for each test case, n and k are integers satisfying 1 ≤ k ≤ n ≤ 1000.
def func():
    for _ in range(int(input())):
        n, k = map(int, stdin.readline().split())
        
        ans = [x for x in range(1, k // 2 + 1)] + [x for x in range(k + 1, n + 1)]
        
        print('%d\n%s' % (len(ans), ' '.join(map(str, ans))))
        
    #State of the program after the  for loop has been executed: `T` is an integer such that 1 ≤ T ≤ 100, `n` is an integer within the range 1 to 1000, `k` is an integer within the range 1 to 1000, and 1 ≤ k ≤ n ≤ 1000, `ans` is a list of integers from 1 to `k // 2 + 1` followed by integers from `k + 1` to `n + 1`, the output is `n - k // 2 + 1` followed by the elements of `ans` joined into a single string separated by spaces.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers `n` and `k` where \(1 \leq k \leq n \leq 1000\). For each test case, it generates a list `ans` containing integers from 1 to `k // 2 + 1` followed by integers from `k + 1` to `n`. The function then prints the length of `ans` followed by the elements of `ans` concatenated into a single line separated by spaces. The function accepts no direct parameters but reads the number of test cases `T` (where \(1 \leq T \leq 100\)) from standard input at the beginning. The final state of the program after the function concludes is that it has processed all test cases, printing the required output for each case.

