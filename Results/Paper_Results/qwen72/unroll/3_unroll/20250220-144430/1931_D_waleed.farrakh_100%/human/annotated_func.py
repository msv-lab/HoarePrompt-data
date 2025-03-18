#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer such that 2 ≤ n ≤ 2 · 10^5), x (an integer such that 1 ≤ x ≤ 10^9), y (an integer such that 1 ≤ y ≤ 10^9), and arr (a list of integers such that 1 ≤ len(arr) ≤ n and 1 ≤ arr[i] ≤ 10^9 for all 0 ≤ i < len(arr)).
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
        
    #State: `results` is a list containing the count of pairs for each test case, where the count is the number of elements in the array `arr` that have the same remainders when divided by `x` and `y` as some other element in the array. The `test_cases` list remains unchanged.
    return results
    #The program returns the list `results` which contains the count of pairs for each test case, where the count is the number of elements in the array `arr` that have the same remainders when divided by `x` and `y` as some other element in the array.
#Overall this is what the function does:The function `func_1` accepts a list of test cases, where each test case is a tuple containing an integer `n`, two integers `x` and `y`, and a list of integers `arr`. It returns a list `results` where each element corresponds to the count of pairs in the respective `arr` that have the same remainders when divided by `x` and `y`. The original `test_cases` list remains unchanged.

#State of the program right berfore the function call: No variables are passed to the function `func_2`.
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
        
    #State: Output State: `test_cases` is a list containing `t` tuples, where each tuple is of the form `(n, x, y, arr)`. `n`, `x`, and `y` are integers derived from the second, third, and fourth values of each pair of lines in `data`, starting from the second line. `arr` is a list of integers derived from the third line of each pair of lines in `data`. `idx` is `1 + 2 * t`. `input` remains a reference to `sys.stdin.read`, and `data` remains the same list of strings as in the initial state.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `test_cases` is a list containing `t` tuples, where each tuple is of the form `(n, x, y, arr)`. `n`, `x`, and `y` are integers derived from the second, third, and fourth values of each pair of lines in `data`, starting from the second line. `arr` is a list of integers derived from the third line of each pair of lines in `data`. `idx` is `1 + 2 * t`. `input` remains a reference to `sys.stdin.read`. `data` remains the same list of strings as in the initial state. `results` is the value returned by `func_1(test_cases)`.
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes it into a list of test cases, and prints the results of applying `func_1` to these test cases. Each test case is a tuple containing integers `n`, `x`, `y`, and a list of integers `arr`. The function does not accept any parameters and does not return any value. After the function concludes, the input data is processed and the results are printed to the standard output.

