#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. Each test case consists of n (1 ≤ n ≤ 2 ⋅ 10^5), an integer representing the size of the array a, followed by n integers a_1, a_2, \ldots, a_n (0 ≤ a_i < n), where the sum of n over all test cases does not exceed 2 ⋅ 10^5.
def func_1():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(N):
        cnt[a[i]] += 1
        
    #State: Output State: The loop will have executed all its iterations, meaning `i` will be equal to `N-1`. For each element `a[i]` in the list `a`, the value of `cnt[a[i]]` will be incremented by 1 for every occurrence of `a[i]` in the list `a`. Therefore, `cnt` will contain the count of each integer present in the list `a`.
    #
    #In natural language, after the loop executes all its iterations, `t` remains a positive integer such that \(1 \leq t \leq 2 \cdot 10^4\), `N` is the number of elements in the list `a`, `a` is a list of integers obtained from the input split and mapped to integers, `cnt` is a `defaultdict` where each key is an integer from the list `a` and its corresponding value is the count of how many times that integer appears in `a`.
    t = 0
    for i in range(N + 1):
        if cnt[i] == 1:
            t += 1
        
        if t >= 2 or cnt[i] == 0:
            return i
        
    #State: The loop has completed all its iterations, and the function has returned 2.
#Overall this is what the function does:The function processes an input array of integers and counts the occurrences of each integer in the array using a `defaultdict`. It then iterates through the possible values (0 to N) and checks the count of each value. If a value occurs exactly once, it increments a counter `t`. Once `t` reaches 2 or if a value does not occur at all, the function returns that value. If no such value is found, the function returns 2. The function ultimately returns either 0, 1, or 2 based on the conditions met during its execution.

