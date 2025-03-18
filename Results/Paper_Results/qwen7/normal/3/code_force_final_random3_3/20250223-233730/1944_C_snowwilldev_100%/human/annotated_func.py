#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a is a list of n non-negative integers where each integer is less than n. The sum of all n values across all test cases does not exceed 2⋅10^5.
def func_1():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(N):
        cnt[a[i]] += 1
        
    #State: Output State: After the loop executes all its iterations, `t` is a positive integer such that \(1 \leq t \leq 2 \cdot 10^4\), `N` is a positive integer representing the number of elements in the list `a`, `a` is a list of integers obtained from splitting the input string and converting each element to an integer, `cnt` is a defaultdict with default value 0 where each key is an integer from the list `a` and the corresponding value is the count of how many times that integer appears in the list `a`.
    #
    #In simpler terms, after all iterations of the loop, the `cnt` dictionary will contain each unique integer from the list `a` as a key, and the value associated with each key will be the total count of occurrences of that integer in the list `a`.
    t = 0
    for i in range(N + 1):
        if cnt[i] == 1:
            t += 1
        
        if t >= 2 or cnt[i] == 0:
            return i
        
    #State: t is 4, N is a positive integer, `a` is a list of integers, `cnt` is a defaultdict with default value 0 where each key is an integer from the list `a` and the corresponding value is the count of how many times that integer appears in the list `a`.
#Overall this is what the function does:The function processes a list `a` of integers and an integer `t`. It counts the occurrences of each integer in the list `a` and updates a `defaultdict` `cnt`. The function then iterates through the possible values in `a` and checks if the count of the current value is not 1 and if the condition `(t >= 2 or cnt[i] == 0)` is met. If such a value is found, it is returned. If no such value exists, the function returns 1. If the count of any value in `a` is exactly 1, `t` is set to 4 and that value is returned.

