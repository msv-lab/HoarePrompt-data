#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 3 · 10^5, and a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    input = sys.stdin.read
    data = input().split()
    current_index = 0
    t = int(data[current_index])
    current_index += 1
    results = []
    for _ in range(t):
        hashing = {}
        
        n = int(data[current_index])
        
        current_index += 1
        
        a = []
        
        for i in range(n):
            a.append(int(data[current_index]))
            current_index += 1
        
        a.sort()
        
        ans = 0
        
        for i in range(n - 1):
            if a[i] not in hashing:
                hashing[a[i]] = 0
            hashing[a[i]] += i
            if a[i] == a[i + 1]:
                ans += hashing[a[i]]
        
        results.append(ans)
        
    #State: After the loop has executed all `t` iterations, `current_index` is `1 + t * (1 + n)`, `results` is a list containing `t` elements, each of which is the `ans` calculated for each iteration, `t` is 0 (as the loop has completed all iterations), `n` is the last value of `n` processed, `a` is the last sorted list of integers processed, `i` is `n - 1`, `ans` is 0 (reset after each iteration), and `hashing` is an empty dictionary (reset after each iteration). The `data` list remains unchanged.
    for result in results:
        print(result)
        
    #State: `results` is a list containing `t` elements, where `t` is the total number of iterations the loop has executed. Each element in the `results` list is the `ans` value calculated during each iteration of the loop. The `data` list remains unchanged, and the other variables (`current_index`, `n`, `a`, `i`, `ans`, and `hashing`) are in their final states as described in the initial state.
#Overall this is what the function does:The function reads input from standard input, processes multiple test cases, and prints the results. Each test case involves reading an integer `n` and a list of `n` integers. The function calculates a specific value for each test case based on the sorted list of integers and prints these values. The function does not return any value; instead, it directly prints the results to the standard output. After processing all test cases, the function leaves the input data unchanged and resets all internal variables used for processing each test case.

