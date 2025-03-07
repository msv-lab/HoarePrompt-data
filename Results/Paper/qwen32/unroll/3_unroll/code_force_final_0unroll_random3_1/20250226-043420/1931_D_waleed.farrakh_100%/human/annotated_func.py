#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains an integer n (2 <= n <= 2 * 10^5), two positive integers x and y (1 <= x, y <= 10^9), and a list arr of n integers (1 <= a_i <= 10^9).
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
        
    #State: results is a list containing the count of pairs of elements in each arr that have the same remainders when divided by x and y.
    return results
    #The program returns a list named 'results' that contains the count of pairs of elements in each array 'arr' that have the same remainders when divided by 'x' and 'y'.
#Overall this is what the function does:The function accepts a list of test cases, where each test case consists of an integer `n`, two positive integers `x` and `y`, and a list `arr` of `n` integers. It calculates and returns a list containing the count of pairs of elements in each `arr` that have the same remainders when divided by `x` and `y`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, x and y are integers such that 1 <= x, y <= 10^9, and arr is a list of integers of length n where each element a_i satisfies 1 <= a_i <= 10^9.
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
        
    #State: `n`, `x`, `y`, and `arr` are the values from the last test case processed, `test_cases` is a list of tuples containing all test cases, and `idx` is `1 + 2*t`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `n`, `x`, `y`, and `arr` remain unchanged from the initial state, `test_cases` remains the same list of tuples, `idx` remains `1 + 2*t`, and `results` is the output of `func_1(test_cases)`. The loop has printed each element of `results` to the console.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of integers `n`, `x`, `y`, and a list of integers `arr` of length `n`. It processes these test cases using another function `func_1` and prints the results for each test case.

