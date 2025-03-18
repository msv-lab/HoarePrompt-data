#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer such that 2 ≤ n ≤ 2 · 10^5), x (an integer such that 1 ≤ x ≤ 10^9), y (an integer such that 1 ≤ y ≤ 10^9), and arr (a list of integers such that 1 ≤ a_i ≤ 10^9 and len(arr) = n). The length of test_cases is at most 10^4, and the sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `test_cases` is a list of tuples, `results` is a list containing the final value of `count` for each tuple in `test_cases`, and `freq` is a dictionary that contains the frequency of each `(a % x, a % y)` pair for the last tuple in `test_cases`.
    return results
    #The program returns the list `results` which contains the final value of `count` for each tuple in `test_cases`.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases`, where each tuple contains four elements: `n` (an integer), `x` (an integer), `y` (an integer), and `arr` (a list of integers). For each tuple, the function calculates the number of pairs `(a, b)` in `arr` such that `(-a % x + x) % x == a % x` and `a % y == b % y`, and appends this count to the `results` list. The function returns the `results` list, which contains the final count for each tuple in `test_cases`. After the function concludes, `test_cases` remains unchanged, and `results` contains the counts as described.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads from standard input, expecting a specific format where the first line is an integer t representing the number of test cases, followed by t pairs of lines, each pair containing the integers n, x, y and a list of n integers arr.
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
        
    #State: `t` must be greater than 0, `idx` is 7 + 2 * (t - 3), `test_cases` is a list containing `t` tuples, where each tuple is `(n, x, y, arr)`. For each tuple, `n`, `x`, and `y` are integers derived from splitting and converting the corresponding line in `data`, and `arr` is a list of integers derived from splitting and converting the next line in `data`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `t` must be greater than 0, `test_cases` is a list containing at least one tuple, `results` is an iterable with at least `t` elements, and all elements in `results` have been printed.
#Overall this is what the function does:The function `func_2` reads multiple test cases from standard input, where each test case consists of two lines: the first line contains three integers `n`, `x`, and `y`, and the second line contains a list of `n` integers `arr`. It processes each test case by calling `func_1` with the list of test cases and prints the results of `func_1` for each test case. After the function concludes, all elements in the `results` iterable have been printed, and the state of the program includes the number of test cases `t` being greater than 0, `test_cases` being a list of `t` tuples, and `results` being an iterable with at least `t` elements.

