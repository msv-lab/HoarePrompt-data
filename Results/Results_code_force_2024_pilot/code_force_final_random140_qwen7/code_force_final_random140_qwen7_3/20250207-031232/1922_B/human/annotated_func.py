#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and a list contains n integers a_1, a_2, ..., a_n where 0 ≤ a_i ≤ n. The sum of all n values over all test cases does not exceed 3 ⋅ 10^5.
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
        
    #State: Output State: `current_index` is 68, `t` is an integer such that \(1 \leq t \leq 10^4\), `results` is a list containing the final answer `[final_ans]` repeated `t` times, `hashing` is an empty dictionary, `a` is a sorted list containing integers from `data[47]` to `data[63]`, `n` is the integer value of `data[47]`, `i` is `n + 2` initially but changes during the loop iterations.
    #
    #This output state indicates that the loop has completed all its iterations. The `current_index` is now 68, which means it has processed all the data up to the last element. The `results` list contains the final answer calculated by the loop, repeated `t` times, as the loop runs `t` times. The `hashing` dictionary is empty because no more pairs of consecutive equal elements were found in the remaining data. The list `a` contains the last set of integers processed, sorted, and `n` is the count of these integers. The variable `i` starts at `n + 2` for the first iteration of the inner loop but increments with each pass through the loop.
    for result in results:
        print(result)
        
    #State: The `results` list contains the final answer calculated by the loop, repeated `t` times, and the loop has completed all its iterations.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` (number of test cases), an integer `n` (length of the list), and a list of `n` integers `a_1, a_2, ..., a_n`. For each test case, it sorts the list of integers and calculates a specific value based on the sorted list. This value is related to the cumulative sum of indices where consecutive identical elements are found. The function then prints the calculated value for each test case.

