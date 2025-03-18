#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the length of the array), x and y (two integers representing Polycarp's favorite integers), and arr (a list of n integers representing the elements of the array). Each element in arr is an integer between 1 and 10^9 inclusive.
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
        
    #State: Output State: `results` is a list of integers, where each integer represents the value of `count` calculated for each corresponding test case in `test_cases`. For each test case, the value of `count` is determined by counting the number of pairs `(rx, ry)` that have appeared before in the array `arr`, with `rx` being the result of `(-a % x + x) % x` and `ry` being the result of `a % y`.
    return results
    #The program returns a list of integers named 'results', where each integer represents the count of pairs (rx, ry) that have appeared before in the array 'arr' for each corresponding test case in 'test_cases'. Here, rx is calculated as `(-a % x + x) % x` and ry as `a % y`.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases` as input. Each tuple contains the length of an array `n`, two integers `x` and `y` representing Polycarp's favorite numbers, and an array `arr` of integers. For each test case, the function calculates the count of unique pairs `(rx, ry)` that appear in the array `arr`, where `rx` is computed as `(-a % x + x) % x` and `ry` as `a % y`. It then appends this count to a list `results`. After processing all test cases, the function returns the list `results`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 2 ≤ n ≤ 2·10^5, x and y are integers such that 1 ≤ x, y ≤ 10^9, and arr is a list of n integers such that 1 ≤ arr[i] ≤ 10^9 for all 0 ≤ i < n.
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
        
    #State: Output State: `test_cases` is a list of tuples, where each tuple contains four elements: `n`, `x`, `y`, and `arr`. Each `arr` is a list of `n` integers. The value of `idx` is `2 * t + 1`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: The output state will be the same as the initial execution state because the loop only prints the results from the `results` list without modifying any variables. The `results` list is the return value of `func_1(test_cases)`, and the loop simply iterates over and prints its contents. No new values are assigned or variables are altered within the loop.
#Overall this is what the function does:The function reads input from stdin, processes multiple test cases, and then calls another function `func_1` to process these test cases. It collects the results from `func_1` and prints them out. The function does not return any value explicitly.

