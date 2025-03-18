#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 2 · 10^4, representing the number of test cases. Each test case consists of an integer n where 1 ≤ n ≤ 2 · 10^5, and a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        counter = {}
        
        for i in arr:
            counter[i] = counter.get(i, 0) + 1
        
        ans = 0
        
        once = False
        
        for i in range(n):
            if counter.get(i, 0) == 0:
                ans = i
                break
            elif counter.get(i, 0) == 1 and not once:
                once = True
                ans = i + 1
            elif counter.get(i, 0) == 1:
                ans = i
                break
        
        print(ans)
        
    #State: After all iterations of the loop have completed, `t` is 0, `n` is the last input integer for the final test case, `arr` is the last list of integers from the final test case, `counter` contains the frequency count of each element in the last `arr`, `i` is the last element of the last `arr`, `ans` is the smallest non-negative integer that either does not appear in the last `arr` or appears exactly once (if `once` is True), and `once` is True if there was at least one unique element in the last `arr`.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then finds the smallest non-negative integer that either does not appear in the list or appears exactly once. If there are multiple such integers, it chooses the smallest one. The function prints the result for each test case. After processing all test cases, the function terminates.

