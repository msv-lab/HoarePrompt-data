#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3⋅10^5, and a list contains n integers a_1, a_2, ..., a_n where 0 ≤ a_i ≤ n. Additionally, the sum of all n values over all test cases does not exceed 3⋅10^5.
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
        
    #State: Output State: The loop has executed all its iterations, resulting in the `results` list containing the cumulative sum of `ans` for each iteration. Specifically, `results` will contain the values of `ans` calculated after each iteration of the loop. The variable `i` will be equal to `n - 1` after the final iteration, indicating that the innermost loop has processed all elements in the list `a`. The `hashing` dictionary will be empty since it is reinitialized at the start of each iteration of the outer loop. The variable `ans` will hold the final cumulative sum of the values in `hashing` for elements that are consecutive in the list `a` across all iterations. The list `a` will be fully processed, and `current_index` will reflect the total number of elements processed, which is the sum of `n` for each iteration.
    for result in results:
        print(result)
        
    #State: The loop has executed all its iterations, resulting in the `results` list containing the cumulative sum of `ans` for each iteration. Specifically, `results` will contain the values of `ans` calculated after each iteration of the loop. The variable `i` will be equal to `n - 1` after the final iteration, indicating that the innermost loop has processed all elements in the list `a`. The `hashing` dictionary will be empty since it is reinitialized at the start of each iteration of the outer loop. The variable `ans` will hold the final cumulative sum of the values in `hashing` for elements that are consecutive in the list `a` across all iterations. The list `a` will be fully processed, and `current_index` will reflect the total number of elements processed, which is the sum of `n` for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t, another integer n, and a list of n integers a. For each test case, it sorts the list a and calculates the cumulative sum of specific values based on the sorted list. The function then prints the result for each test case. The final state of the program is that it outputs the calculated results for all test cases.

