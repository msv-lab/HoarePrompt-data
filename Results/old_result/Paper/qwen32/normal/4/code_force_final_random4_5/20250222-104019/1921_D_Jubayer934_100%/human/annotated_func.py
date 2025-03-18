#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n and m are integers such that 1 <= n <= m <= 2 * 10^5. a_i is a list of n integers where each a_i satisfies 1 <= a_i <= 10^9. b_i is a list of m integers where each b_i satisfies 1 <= b_i <= 10^9. The sum of m over all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        temp = -1
        
        ans = []
        
        a = sorted(map(int, input().split()))[:n]
        
        b = sorted(map(int, input().split()), reverse=True)[:m]
        
        for i in range(n):
            if abs(a[i] - b[-(n - i)]) > abs(a[i] - b[i]):
                temp = i
                break
            ans.append(abs(a[i] - b[i]))
        
        if temp != -1:
            for i in range(temp, n):
                ans.append(abs(a[i] - b[-(n - i)]))
        
        print(sum(ans))
        
    #State: The loop has executed `t` times, where `t` is the number of test cases. For each test case, `n` and `m` are the lengths of the lists `a` and `b` respectively. `a` is a sorted list of `n` integers, and `b` is a sorted list of `m` integers in descending order. `temp` is either -1 or the index `i` where the condition `abs(a[i] - b[-(n - i)]) > abs(a[i] - b[i])` was met during the inner loop. `ans` is a list of absolute differences calculated as follows: for each index `i` from 0 to `temp-1`, `ans` includes `abs(a[i] - b[i])`. If `temp` is not -1, `ans` also includes `abs(a[i] - b[-(n - i)])` for each index `i` from `temp` to `n-1`. The final output for each test case is the sum of all elements in `ans`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two lists of integers `a` and `b`. For each test case, it calculates a series of absolute differences between elements of the two lists and outputs the sum of these differences. The differences are calculated in a specific way: for each element in `a`, it compares the absolute difference with the corresponding element in the front of `b` versus the corresponding element in the back of `b`, and chooses the smaller one until a larger difference is found, after which it switches to choosing from the back of `b`.

