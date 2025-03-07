#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n, x, y, and arr. n is an integer such that 2 ≤ n ≤ 2 · 10^5, x and y are integers such that 1 ≤ x, y ≤ 10^9, and arr is a list of integers of length n, with each element a_i such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: `test_cases` is a list of tuples with at least the number of tuples it started with, `results` is a list containing the final `count` value for each tuple in `test_cases`, and `freq` is a dictionary that contains the frequency of each `(a % x, a % y)` pair for all elements `a` in the corresponding `arr` for each tuple.
    return results
    #The program returns a list named `results` that contains the final `count` value for each tuple in `test_cases`. Each `count` value represents the number of times a specific `(a % x, a % y)` pair occurred in the corresponding `arr` for each tuple.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases`, where each tuple contains four elements: `n`, `x`, `y`, and `arr`. It processes each tuple to count the number of pairs `(a % x, a % y)` in the list `arr` that have previously occurred. The function returns a list `results` where each element is the count of such occurrences for the corresponding tuple in `test_cases`. The input `test_cases` remains unchanged, and the final state of the program includes the `results` list containing these counts.

#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads input from stdin and processes it to create a list of test cases, where each test case is a tuple containing integers n, x, y, and a list of integers arr.
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
        
    #State: `data` is a list of lines from the input, `t` is 0, `test_cases` is a list containing `t` tuples of the form `(n, x, y, arr)`, `idx` is `1 + 2 * t`, `n` is the first integer from the line at index `1 + 2 * (i - 1)` of `data` for each `i` from 1 to `t`, `x` is the second integer from the line at index `1 + 2 * (i - 1)` of `data` for each `i` from 1 to `t`, `y` is the third integer from the line at index `1 + 2 * (i - 1)` of `data` for each `i` from 1 to `t`, `arr` is a list of integers from the line at index `2 + 2 * (i - 1)` of `data` for each `i` from 1 to `t`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `t` is greater than 0, `test_cases` is a list containing at least one tuple of the form `(n, x, y, arr)`, `results` is a list containing all the elements that were returned by `func_1(test_cases)`, and the loop has printed each element in `results` exactly once.
#Overall this is what the function does:The function `func_2` reads input from standard input (stdin), processes it to create a list of test cases, and then passes this list to another function `func_1`. Each test case is a tuple containing four elements: three integers `n`, `x`, `y`, and a list of integers `arr`. After receiving the results from `func_1`, it prints each result to the standard output (stdout). The function does not return any value. The final state of the program is that the input has been processed, the results from `func_1` have been printed, and the function has completed its execution.

