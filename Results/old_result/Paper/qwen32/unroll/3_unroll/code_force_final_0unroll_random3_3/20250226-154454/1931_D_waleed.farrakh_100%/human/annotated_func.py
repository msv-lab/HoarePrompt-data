#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x (an integer representing one of Polycarp's favorite integers), y (an integer representing the other favorite integer), and arr (a list of integers representing the elements of the array). It is guaranteed that 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9 for each element a_i in arr.
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
        
    #State: `test_cases` is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x (an integer representing one of Polycarp's favorite integers), y (an integer representing the other favorite integer), and arr (a list of integers representing the elements of the array). `results` is a list of integers where each integer represents the count of previously seen pairs `(rx, ry)` for each test case.
    return results
    #The program returns the list `results`, where each integer in `results` represents the count of previously seen pairs `(rx, ry)` for each test case in `test_cases`.
#Overall this is what the function does:The function `func_1` processes a list of test cases, where each test case consists of an array size `n`, two favorite integers `x` and `y`, and an array `arr`. For each test case, it calculates the count of previously seen pairs `(rx, ry)` for each element in the array, where `rx` is the adjusted remainder of the element when divided by `x`, and `ry` is the remainder of the element when divided by `y`. The function returns a list of these counts, one for each test case.

#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the length of the array), x (an integer representing one of Polycarp's favorite integers), y (an integer representing the other favorite integer), and arr (a list of n integers representing the elements of the array).
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
        
    #State: `test_cases` is a list of tuples, where each tuple contains four elements: `n`, `x`, `y`, and `arr`. Each tuple represents the parsed data for one test case. `input` remains unchanged as the content read from standard input. `data` remains unchanged as a list where each element is a line from the input content. `t` remains unchanged as an integer representing the number of test cases. `idx` is now `2 * t + 1`, reflecting the position after processing all test cases.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: The output state is such that each result from the `results` list is printed on a new line. The variables `test_cases`, `input`, `data`, `t`, and `idx` remain unchanged.
#Overall this is what the function does:The function reads input from standard input, parses it into a list of test cases, and then processes each test case to produce a result. Each test case consists of an integer `n`, two favorite integers `x` and `y`, and a list `arr` of `n` integers. The results of processing these test cases are printed, one per line.

