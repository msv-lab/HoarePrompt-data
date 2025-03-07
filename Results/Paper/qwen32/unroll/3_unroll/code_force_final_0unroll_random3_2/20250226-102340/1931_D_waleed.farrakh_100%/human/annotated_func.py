#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x (an integer representing Polycarp's first favorite integer), y (an integer representing Polycarp's second favorite integer), and arr (a list of integers of length n).
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
        
    #State: `test_cases` is a list of tuples, where each tuple contains four elements: `n` (an integer representing the size of the array), `x` (an integer representing Polycarp's first favorite integer), `y` (an integer representing Polycarp's second favorite integer), and `arr` (a list of integers of length `n`); `results` is a list of integers, where each integer is the count of previously seen pairs of remainders for the corresponding test case.
    return results
    #The program returns `results`, which is a list of integers. Each integer in the list represents the count of previously seen pairs of remainders for the corresponding test case in `test_cases`.
#Overall this is what the function does:The function processes a list of test cases, where each test case includes an array and two integers. For each test case, it calculates the count of previously seen pairs of remainders when each element in the array is divided by the two integers. The function returns a list of these counts, one for each test case.

#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x (an integer representing one of Polycarp's favorite integers), y (an integer representing the other favorite integer), and arr (a list of n integers representing the elements of the array). Each tuple corresponds to a test case.
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
        
    #State: `test_cases` is a list of tuples, each containing `(n, x, y, arr)` for each test case, `data` is unchanged, `t` is unchanged, `idx` is `1 + 2*t`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `test_cases` is a list of tuples, each containing `(n, x, y, arr)` for each test case; `data` is unchanged; `t` is unchanged; `idx` is `1 + 2*t`; `results` is the output of `func_1(test_cases)`.
#Overall this is what the function does:The function `func_2` reads input from standard input, processes multiple test cases, and prints the results. Each test case consists of an integer `n`, two favorite integers `x` and `y`, and a list of `n` integers. The function collects these test cases, passes them to `func_1` for processing, and outputs the results returned by `func_1`.

