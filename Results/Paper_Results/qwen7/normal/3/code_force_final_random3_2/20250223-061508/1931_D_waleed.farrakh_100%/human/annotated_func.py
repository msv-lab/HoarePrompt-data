#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x and y (two integers representing Polycarp's favorite integers), and arr (a list of n integers representing the elements of the array). Each element in arr is an integer such that 1 <= a_i <= 10^9.
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
        
    #State: After the loop executes all iterations, `arr` will be an empty list, `rx` will be the last calculated value of (-a % x + x) % x, `ry` will be the last calculated value of a % y, `count` will be the sum of `freq[rx, ry]` for all pairs where `rx` and `ry` match any previously seen pairs, `current_pair` will be the last calculated pair of (a % x, a % y), and `results` will contain the final value of `count`. The dictionary `freq` will store the frequency of each unique (a % x, a % y) pair seen throughout the loop.
    return results
    #The program returns the final value of `count`, which represents the sum of frequencies of all unique (a % x, a % y) pairs seen throughout the loop.
#Overall this is what the function does:The function processes a list of test cases, where each test case includes an array of integers and two favorite integers x and y. For each test case, it calculates the frequency of unique pairs (a % x, a % y) for each element a in the array. It then sums up the frequencies of these unique pairs and returns this sum as the final result.

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
        
    #State: Output State: `t` is 0, `idx` is equal to `2 * t` which is 4 (since `t` is 0), `n`, `x`, `y` are integers, `arr` is a list of integers obtained by splitting `data[idx + 1]` and converting each element to an integer, `test_cases` is a list containing `t` tuples, each tuple being `(n, x, y, arr)` where `n`, `x`, `y`, and `arr` are as described above.
    #
    #In simpler terms, after the loop completes all its iterations, `t` becomes 0 because it was decremented by 1 in each iteration until it reached 0. The index `idx` will be 4 since it increments by 2 in each iteration and we start with `t` as 1, making it go through 3 iterations in total. The variables `n`, `x`, `y`, and `arr` will hold the values from the last iteration of the loop. The list `test_cases` will contain `t` (which is 0) tuples, but since `t` is 0, `test_cases` will be an empty list.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: Output State: `t` is 0, `idx` is 4, `n`, `x`, `y`, and `arr` are as they were in the last iteration of the loop, `test_cases` is an empty list, `results` contains at least 3 elements.
    #
    #Natural Language Explanation: After the loop has executed all its iterations, the variable `t` remains unchanged at 0, `idx` remains at 4, and `n`, `x`, `y`, and `arr` retain their state from the last iteration of the loop. The `test_cases` list remains empty since it was not modified within the loop. The key change is that the `results` list now contains at least 3 elements, as the loop iterated at least 3 times to produce these outputs.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `t`, followed by `t` sets of integers `n`, `x`, `y`, and a list `arr`. It then processes these test cases using `func_1`, which is not defined in this snippet, and prints the results returned by `func_1`. The function ensures that all input constraints are respected and organizes the test cases into a structured format before passing them to `func_1`. After processing, the function outputs the results of `func_1` for each test case.

