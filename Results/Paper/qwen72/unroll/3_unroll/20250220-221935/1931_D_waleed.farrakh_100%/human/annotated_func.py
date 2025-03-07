#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n, x, y, and arr. n is an integer such that 2 ≤ n ≤ 2 · 10^5, x and y are integers such that 1 ≤ x, y ≤ 10^9, and arr is a list of integers of length n, where each element a_i satisfies 1 ≤ a_i ≤ 10^9.
def func_1(test_cases):
    results = []
    for (n, x, y, arr) in test_cases:
        freq = {}
        
        count = 0
        
        for a in arr:
            rx = (-a % x + x) % x
            ry = a % y
            if (rx, ry) in freq:
                count += freq[rx, ry]
            current_pair = a % x, a % y
            if current_pair in freq:
                freq[current_pair] += 1
            else:
                freq[current_pair] = 1
        
        results.append(count)
        
    #State: results is a list containing the count of pairs (a_i, a_j) for each test case, where 0 ≤ i < j < n and (a_i + a_j) is divisible by both x and y. The other variables (test_cases) remain unchanged.
    return results
    #The program returns the list 'results', which contains the count of pairs (a_i, a_j) for each test case, where 0 ≤ i < j < n and (a_i + a_j) is divisible by both x and y. The other variables (test_cases) remain unchanged.
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case is a tuple containing an integer `n`, two integers `x` and `y`, and a list `arr` of length `n`. It returns a list `results` where each element is the count of pairs `(a_i, a_j)` in `arr` such that `(a_i + a_j)` is divisible by both `x` and `y`. The input `test_cases` remain unchanged after the function execution.

#State of the program right berfore the function call: None of the variables are used in the function signature of `func_2`. The function reads input from stdin, processes it to extract test cases, and calls another function `func_1` with the processed test cases.
def func_2():
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    test_cases = []
    idx = 1
    for _ in range(t):
        n, x, y = map(int, data[idx].split())
        
        arr = list(map(int, data[idx + 1].split()))
        
        test_cases.append((n, x, y, arr))
        
        idx += 2
        
    #State: `t` is the integer value of the first string in `data`. `test_cases` is a list of tuples, each containing four elements: `n`, `x`, `y`, and `arr`, where `n`, `x`, and `y` are integers from the corresponding line in `data`, and `arr` is a list of integers from the next line in `data`. `idx` is `1 + 2 * t`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `t` remains the same, `test_cases` remains the same, `idx` remains the same, and `results` has been fully iterated over, with each element printed to the console.
#Overall this is what the function does:The function `func_2` reads input from stdin, processes it to extract multiple test cases, and calls another function `func_1` with these test cases. Each test case is a tuple containing four elements: `n`, `x`, `y`, and `arr`, where `n`, `x`, and `y` are integers, and `arr` is a list of integers. The function then prints each result returned by `func_1` to the console. The function does not return any value. After the function concludes, the input data is processed, and the results of `func_1` are printed to the console.

