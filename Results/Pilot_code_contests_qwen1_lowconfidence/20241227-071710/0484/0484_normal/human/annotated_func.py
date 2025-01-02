#State of the program right berfore the function call: T is an integer such that 1 ≤ T ≤ 100, and each test case consists of two integers n and k where 1 ≤ k ≤ n ≤ 1000.
def func():
    for _ in range(int(input())):
        n, k = map(int, stdin.readline().split())
        
        ans = [x for x in range(1, k // 2 + 1)] + [x for x in range(k + 1, n + 1)]
        
        print('%d\n%s' % (len(ans), ' '.join(map(str, ans))))
        
    #State of the program after the  for loop has been executed: `T` is an integer such that \(1 \leq T \leq 100\); `n` and `k` are the last two integers input; `ans` is a list containing integers from `1` to `k // 2 + 1` followed by integers from `k + 1` to `n + 1`; no further inputs are read.
#Overall this is what the function does:The function processes a series of test cases where `T` is an integer such that 1 ≤ T ≤ 100. For each test case, it reads two integers `n` and `k` where 1 ≤ k ≤ n ≤ 1000. It then constructs a list `ans` containing integers from `1` to `k // 2 + 1` followed by integers from `k + 1` to `n + 1`. Finally, it prints the length of `ans` followed by the elements of `ans` separated by spaces. After processing all test cases, the program stops reading further inputs. Potential edge cases include when `k` is even or odd, and when `T` is at its minimum or maximum value. The function handles these cases by correctly constructing the list `ans` based on the given values of `n` and `k`.

