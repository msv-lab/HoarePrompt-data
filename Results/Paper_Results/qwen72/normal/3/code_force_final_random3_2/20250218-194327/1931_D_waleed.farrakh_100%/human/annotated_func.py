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
        
    #State: `test_cases` is a list of tuples with at least the number of tuples it started with, `results` is a list containing the value of `count` for each tuple in `test_cases`, and `freq` is a dictionary that contains the frequency of each `(a % x, a % y)` pair for the last processed tuple `(n, x, y, arr)`.
    return results
    #The program returns a list `results` that contains the value of `count` for each tuple in `test_cases`. `results` reflects the number of elements in each tuple's array `arr` that satisfy the condition `(a % x, a % y)` for the corresponding `(n, x, y, arr)` tuple in `test_cases`.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `test_cases`, where each tuple contains integers `n`, `x`, `y`, and a list of integers `arr`. It returns a list `results` where each element is the count of pairs of elements in `arr` that satisfy the condition `(-a % x + x) % x == a % x` and `a % y == b % y` for the corresponding tuple `(n, x, y, arr)` in `test_cases`. The original `test_cases` list remains unchanged.

#State of the program right berfore the function call: None of the variables in the function signature are used. The function reads from standard input and processes multiple test cases, each consisting of an integer n, two integers x and y, and an array arr of n integers.
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
        
    #State: `data` is a list of strings, `t` is the integer value of the first element in `data` and must be greater than or equal to the number of iterations, `test_cases` is a list containing `t` tuples, each tuple is `(n, x, y, arr)`, where `n`, `x`, and `y` are integers derived from the corresponding parts of the strings at `data[1], data[3], ...`, and `arr` is a list of integers derived from the strings at `data[2], data[4], ...`. `idx` is `2 * t + 1`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: `results` must be an iterable with at least `t` elements, and the loop will have printed all `t` elements of `results`.
#Overall this is what the function does:The function `func_2` reads multiple test cases from standard input, where each test case consists of an integer `n`, two integers `x` and `y`, and an array `arr` of `n` integers. It processes these test cases by calling another function `func_1` and prints the results of each test case. After the function concludes, the program has read and processed `t` test cases, and the results of these test cases have been printed to the standard output.

