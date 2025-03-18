#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x (an integer representing one of Polycarp's favorite integers), y (an integer representing the other favorite integer), and arr (a list of n integers representing the elements of the array).
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
        
    #State: - `test_cases` remains unchanged as it is the input list of test cases.
    #- `results` is a list containing one element for each test case in `test_cases`, where each element is the `count` for that specific test case.
    #- `freq` is a dictionary that is re-initialized for each test case and stores the frequency of `(rx, ry)` pairs for the current test case only.
    #- `count` is the total number of times pairs `(rx, ry)` have been seen before for the current test case.
    #
    #In simpler terms, after all the iterations, `results` will contain the count of previously seen `(rx, ry)` pairs for each test case in `test_cases`. The `freq` dictionary is reset for each test case, so it does not retain information across different test cases.
    #
    #Output State:
    return results
    #The program returns `results`, which is a list containing one element for each test case in `test_cases`. Each element in `results` represents the `count` of previously seen `(rx, ry)` pairs for that specific test case.
#Overall this is what the function does:The function processes a list of test cases, where each test case includes an array and two favorite integers. It calculates and returns a list of counts, where each count represents the number of previously seen pairs of remainders when the array elements are divided by the two favorite integers.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, n is an integer representing the size of the array, x and y are positive integers representing Polycarp's favorite integers, and arr is a list of integers representing the elements of the array. For each test case, it is guaranteed that 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9, and 1 <= a_i <= 10^9 for all i in the range of the array.
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
        
    #State: `t` is 0, `n` is the first integer from `data[2*t-1]`, `x` is the second integer from `data[2*t-1]`, `y` is the third integer from `data[2*t-1]`, `arr` is a list of integers from `data[2*t]`, `data` is a list of strings where `data[0]` is the string representation of `t` and the remaining elements are the subsequent lines of input, `test_cases` is a list containing `t` tuples `[(n, x, y, arr), (n, x, y, arr), ..., (n, x, y, arr)]`, `idx` is 2*t.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: All elements in `results` have been printed.
#Overall this is what the function does:The function `func_2` reads multiple test cases from the standard input, where each test case consists of integers `n`, `x`, `y`, and an array `arr`. It processes these test cases by calling `func_1` with a list of tuples containing the test case data. The results from `func_1` are then printed. The function does not modify the input values directly but uses them to produce and print output based on the logic implemented in `func_1`.

