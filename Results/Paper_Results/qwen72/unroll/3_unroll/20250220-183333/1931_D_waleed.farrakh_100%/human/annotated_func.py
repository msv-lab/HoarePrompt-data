#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n, x, y, and arr. n is an integer such that 2 ≤ n ≤ 2 · 10^5, x and y are integers such that 1 ≤ x, y ≤ 10^9, and arr is a list of integers of length n such that 1 ≤ arr[i] ≤ 10^9.
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
        
    #State: Output State: `results` is a list of integers, where each integer represents the count of pairs `(a, b)` in the corresponding `arr` such that `(-a % x + x) % x == a % x` and `a % y == b % y`, and `a` and `b` are distinct elements in `arr`. The length of `results` is equal to the length of `test_cases`. The values in `results` are calculated based on the initial state of `test_cases` and the logic within the loop. The `freq` dictionary is used to keep track of the frequency of pairs `(a % x, a % y)` in each iteration, and `count` is updated accordingly. The final `results` list contains the counts for each test case.
    return results
    #The program returns a list `results` where each element is an integer representing the count of distinct pairs `(a, b)` in the corresponding `arr` from `test_cases` such that `(-a % x + x) % x == a % x` and `a % y == b % y`. The length of `results` is equal to the length of `test_cases`.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases`, where each tuple contains four elements: `n`, `x`, `y`, and `arr`. It returns a list `results` where each element is an integer representing the count of distinct pairs `(a, b)` in the corresponding `arr` such that `(-a % x + x) % x == b % x` and `a % y == b % y`. The length of `results` is equal to the length of `test_cases`. The function does not modify the input `test_cases` and the final state of the program includes the `results` list with the computed counts for each test case.

#State of the program right berfore the function call: No variables are passed to the function `func_2()`. The function reads input from standard input, processes it, and constructs a list of test cases, where each test case is a tuple `(n, x, y, arr)`. `n` is an integer representing the size of the array, `x` and `y` are Polycarp's favorite integers, and `arr` is a list of integers representing the elements of the array.
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
        
    #State: The variable `t` remains unchanged. The variable `test_cases` is a list containing `t` tuples, where each tuple is `(n, x, y, arr)`. Each `n` is an integer representing the size of the array, `x` and `y` are Polycarp's favorite integers, and `arr` is a list of integers representing the elements of the array. The variable `idx` is `1 + 2 * t`. No other variables are affected.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: Output State: The variable `t` remains unchanged. The variable `test_cases` remains unchanged. The variable `idx` remains unchanged. The variable `results` is the same as the output of the function `func_1` when called with `test_cases` as its argument. The loop has printed each element of `results` to the console, one by one.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads input from standard input, processes it, and constructs a list of test cases, where each test case is a tuple `(n, x, y, arr)`. `n` is an integer representing the size of the array, `x` and `y` are Polycarp's favorite integers, and `arr` is a list of integers representing the elements of the array. The function then calls `func_1` with the list of test cases and prints each result from `func_1` to the console. After the function concludes, the variable `t` remains unchanged, `test_cases` contains the constructed test cases, and `results` contains the output of `func_1`. The variable `idx` is `1 + 2 * t`. No other variables are affected.

