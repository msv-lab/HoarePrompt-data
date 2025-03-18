#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where 0 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5.
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
        
    #State: After the loop executes all iterations, `t` is the initial value provided, `n` is the integer value of `data[0]` (the first element of the `data` list), `a` is a sorted list containing `n` elements from the last processed segment of `data`, `current_index` is the index just after the last processed element in `data`, `results` is a list containing `t` elements where each element is the `ans` calculated for each iteration, `i` is `n - 1` for the last iteration, `hashing` is a dictionary containing the cumulative indices for each unique element in the last processed list `a`, and `ans` is the sum of the values in `hashing` for each element in `a` that appears consecutively in the list. The sum of `n` over all test cases does not exceed 3 · 10^5, and `data` remains a list of strings obtained by splitting the input data.
    for result in results:
        print(result)
        
    #State: `results` is a list containing `t` elements, each element being the `ans` calculated for each iteration of the loop.
#Overall this is what the function does:The function reads input from standard input, processes multiple test cases, and prints the result for each case. Each test case involves an integer `n` and a list `a` of `n` integers. The function calculates a specific value `ans` for each test case based on the sorted list `a` and a hash map that tracks the cumulative indices of elements. The final output is a list of these `ans` values, one for each test case. After processing all test cases, the function prints each result. The function does not return any value; it only prints the results.

