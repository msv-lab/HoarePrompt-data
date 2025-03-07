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
        
    #State: `results` is a list containing the cumulative sum of `count` values computed over all iterations of the loop. The variable `freq` retains its final state from the last iteration, while `rx`, `ry`, `count`, and `current_pair` also reflect their final values from the last iteration.
    return results
    #The program returns a list named 'results' which contains the cumulative sum of 'count' values computed over all iterations of the loop. Additionally, the list includes the final states of 'freq', 'rx', 'ry', and 'current_pair' from the last iteration.
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains an integer `n`, two integers `x` and `y`, and a list `arr`. For each tuple, it computes the count of pairs `(a % x, a % y)` in the list `arr` and accumulates these counts. After processing all tuples, it returns a list of these accumulated counts along with the final states of the frequency dictionary `freq`, and the variables `rx`, `ry`, and `current_pair` from the last iteration.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 2 ≤ n ≤ 2·10^5 and 1 ≤ x, y ≤ 10^9. arr is a list of n integers such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: `idx` is equal to `t * 2`, `t` is equal to 0, `data` remains unchanged, `test_cases` is a list containing tuples `(n, x, y, arr)` for each iteration of the loop, where `n`, `x`, and `y` are integers obtained from the split data, and `arr` is a list of integers obtained by splitting `data[idx + 1]` and converting each element to an integer.
    #
    #This means that after the loop has executed all its iterations, `idx` will be twice the original value of `t`, `t` will be reduced to 0 (since it decreases by 1 with each iteration until it reaches 0), `data` will remain unchanged, and `test_cases` will contain a tuple for each iteration of the loop, with each tuple consisting of `n`, `x`, `y`, and `arr`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: The loop will continue to execute as long as `results` contains at least one element. Once `results` no longer contains any elements, the loop will terminate.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer t, followed by t pairs of integers n, x, y, and a list of n integers arr. It then calls another function `func_1` with a list of these test cases and prints the results returned by `func_1`. After processing all test cases, the function terminates.

