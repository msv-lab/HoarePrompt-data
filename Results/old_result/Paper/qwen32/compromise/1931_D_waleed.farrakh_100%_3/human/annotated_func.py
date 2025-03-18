#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x (an integer representing Polycarp's first favorite integer), y (an integer representing Polycarp's second favorite integer), and arr (a list of n integers representing the elements of the array).
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
        
    #State: `test_cases` is an empty list; `results` is a list containing the final accumulated `count` values for each tuple in the initial `test_cases` list; `freq` is undefined as it is re-initialized for each iteration; `count` is undefined as it is re-initialized for each iteration.
    return results
    #The program returns an empty list `results`
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case consists of an integer `n`, two favorite integers `x` and `y`, and a list `arr` of `n` integers. It processes each test case to compute a count based on the remainders of elements in `arr` when divided by `x` and `y`. The function returns a list of these counts for each test case.

#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x (an integer representing Polycarp's first favorite integer), y (an integer representing Polycarp's second favorite integer), and arr (a list of n integers representing the elements of the array). It is guaranteed that for each tuple, 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9 for each element a_i in arr.
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
        
    #State: `test_cases` is a list containing `t` tuples, `data` is a list of strings, `t` is an integer equal to `int(data[0])`, and `idx` is `2 * t + 1`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `test_cases` is a list containing `t` tuples, `data` is a list of strings, `t` is an integer equal to `int(data[0])`, `idx` is `2 * t + 1`, and all elements in `results` have been printed.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n`, two favorite integers `x` and `y`, and a list of `n` integers `arr`. It processes these test cases using another function `func_1` and prints the results for each test case.

