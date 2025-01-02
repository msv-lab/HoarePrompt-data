#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 100, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 1000.
def func():
    for _ in range(int(input())):
        n, k = map(int, stdin.readline().split())
        
        ans = [x for x in range(1, k // 2 + 1)] + [x for x in range(k + 1, n + 1)]
        
        print('%d\n%s' % (len(ans), ' '.join(map(str, ans))))
        
    #State of the program after the  for loop has been executed: `T` is an integer such that \(1 \leq T \leq 100\), for each test case, `n` is the first integer from the input, `k` is the second integer from the input, and `ans` is the list containing numbers from 1 to `k // 2 + 1` followed by numbers from `k + 1` to `n + 1`; the length of `ans` is `n - k // 2 + 2`, and the elements of `ans` are printed as a space-separated string.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of two integers `n` and `k`. For each test case, it constructs a list `ans` containing numbers from 1 to `k // 2 + 1` followed by numbers from `k + 1` to `n`. The length of `ans` is `n - k // 2 + 2`. It then prints the length of `ans` followed by its elements as a space-separated string. The function accepts an integer `T` indicating the number of test cases, where \(1 \leq T \leq 100\). If `k` is greater than or equal to `n`, the constructed list `ans` will only contain numbers from 1 to `n`. If `k` is exactly half of `n`, the list `ans` will contain the first half of numbers from 1 to `n` excluding `k`.

Potential edge cases and missing functionality:
- If `k == n`, the constructed list `ans` will simply be a sequence from 1 to `n`.
- The function correctly handles the case where `k` is greater than or equal to `n`, but no explicit check is mentioned in the annotation for this scenario. However, the code inherently covers this case by stopping the range generation when `x` reaches `n+1`.

