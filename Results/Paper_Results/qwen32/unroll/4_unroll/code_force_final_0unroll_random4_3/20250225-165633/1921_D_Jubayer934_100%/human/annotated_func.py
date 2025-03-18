#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n and m are integers such that 1 <= n <= m <= 2 * 10^5. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. b is a list of m integers where each integer b_i satisfies 1 <= b_i <= 10^9. The sum of m over all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case, the sum of the absolute differences between elements of the two lists as described in the steps above is printed. The variables `t`, `n`, `m`, `a`, and `b` remain unchanged except for their usage within the loop.
#Overall this is what the function does:For each test case, the function calculates and prints the sum of the absolute differences between elements of two lists, `a` and `b`, after sorting `a` in ascending order and `b` in descending order. The function handles multiple test cases as specified by the input integer `t`.

