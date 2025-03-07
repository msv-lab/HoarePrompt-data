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
        
    #State: `test_cases` is an empty list, `results` contains the final count values for each tuple in the original `test_cases` list, `freq` is a dictionary that reflects the frequency of each unique pair `(a % x, a % y)` encountered in the last processed tuple's `arr`, and `count` is the final count for the last processed tuple.
    return results
    #The program returns `results`, which contains the final count values for each tuple in the original `test_cases` list. Since `test_cases` is an empty list, `results` is also an empty list.
#Overall this is what the function does:The function processes a list of test cases, where each test case consists of an integer `n`, two favorite integers `x` and `y`, and an array `arr` of `n` integers. For each test case, it calculates a count based on the frequency of certain pairs derived from the elements of `arr` and the values of `x` and `y`. The function returns a list of these counts, one for each test case. If the input list of test cases is empty, the function returns an empty list.

#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains an integer n (2 <= n <= 2 * 10^5), integers x and y (1 <= x, y <= 10^9), and a list arr of n integers (1 <= a_i <= 10^9).
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
        
    #State: `test_cases` is a list containing `t` tuples `((n, x, y, arr), ...)`, `input` is a string containing the entire input, `data` is a list of strings, each representing a line from the `input`, `t` is the integer value of `data[0]`, `idx` is `1 + 2*t`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `test_cases` is a list containing `t` tuples `((n, x, y, arr), ...)`, `t` must be greater than 0, `results` must contain `t` elements.
#Overall this is what the function does:The function `func_2` reads input from standard input, processes it to extract multiple test cases, and then calls another function `func_1` with these test cases. Each test case consists of an integer `n`, two integers `x` and `y`, and a list `arr` of `n` integers. The function prints the results returned by `func_1` for each test case.

