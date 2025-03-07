#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x and y (two integers representing Polycarp's favorite integers), and arr (a list of n integers representing the elements of the array). Each element in arr is an integer between 1 and 10^9 inclusive.
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
        
    #State: Output State: `results` is a list of integers, where each integer represents the value of `count` calculated for each corresponding test case in `test_cases`. For each test case, the value of `count` is determined by counting how many pairs `(rx, ry)` appear more than once during the iteration over the array `arr`, with `rx = (-a % x + x) % x` and `ry = a % y`.
    return results
    #The program returns a list of integers called 'results', where each integer represents the count of pairs (rx, ry) that appear more than once for each corresponding test case in 'test_cases'. For each test case, rx is calculated as (-a % x + x) % x and ry is calculated as a % y.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases`, where each tuple contains the size of an array `n`, two integers `x` and `y`, and an array `arr` of integers. For each test case, it calculates the count of unique pairs `(rx, ry)` that appear more than once in the array `arr`. Here, `rx` is computed as `(-a % x + x) % x` and `ry` as `a % y` for each element `a` in `arr`. The function returns a list of integers called `results`, where each integer corresponds to the count of such pairs for each test case.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n, x, and y are integers for each test case such that 2 ≤ n ≤ 2⋅10^5 and 1 ≤ x, y ≤ 10^9; arr is a list of integers such that 1 ≤ a_i ≤ 10^9 for each element a_i in the list, and the length of arr is n.
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
        
    #State: Output State: `test_cases` is a list containing tuples of the form (n, x, y, arr), where each tuple corresponds to the values of `n`, `x`, `y`, and `arr` extracted from `data`. `idx` is `2 * t + 1`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: The output state will be the same as the initial state because the loop only prints the results from the `results` list without modifying any variables. The `results` list is derived from `func_1(test_cases)` and remains unchanged during the loop execution.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `t` indicating the number of test cases, followed by `n`, `x`, `y`, and an array `arr`. It then processes these test cases using `func_1` and prints the results. The function does not return any value but modifies no global state outside of its scope.

