#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers such that 1 ≤ n ≤ m ≤ 2 \cdot 10^5. a_i is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. b_i is a list of m integers where each integer b_i satisfies 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: The loop has executed `t` times, where `t` is an integer such that 1 ≤ t ≤ 100. For each of the `t` test cases, the following holds: `n` is an integer that must be greater than or equal to 1, `m` is an integer such that `n` ≤ `m` ≤ 2 * 10^5, `a` is a list of the first `n` integers from the sorted input, and `b` is a list of the first `m` integers from the input, sorted in descending order. The variable `temp` is either -1 or an integer such that 0 ≤ temp < n. If `temp` is not -1, `ans` is a list containing the values `abs(a[i] - b[i])` for all `i` up to the point where the loop breaks or completes, and includes `abs(a[i] - b[-(n - i)])` for all `i` in the range from `temp` to `n-1`. If `temp` is -1, `ans` contains the values `abs(a[i] - b[i])` for all `i` up to the point where the loop breaks or completes. The final output for each test case is the sum of the elements in `ans`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `m`, and two lists of integers `a` and `b`. For each test case, it calculates the sum of the minimum absolute differences between elements of `a` and `b` following a specific pairing strategy, and prints this sum.

