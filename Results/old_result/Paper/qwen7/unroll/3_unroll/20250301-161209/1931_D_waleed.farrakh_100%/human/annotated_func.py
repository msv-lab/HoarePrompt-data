#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x and y (two integers representing Polycarp's favorite integers), and arr (a list of n integers representing the elements of the array). Each element in arr is an integer such that 1 <= a_i <= 10^9, and n, x, and y satisfy the constraints 2 <= n <= 2 * 10^5, 1 <= x, y <= 10^9.
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
        
    #State: Output State: `test_cases` is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x and y (two integers representing Polycarp's favorite integers), and arr (a list of n integers representing the elements of the array); `results` is a list of integers where each integer represents the value of `count` calculated for each corresponding test case after executing the loop.
    return results
    #The program returns a list of integers where each integer represents the value of `count` calculated for each corresponding test case after executing the loop.
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains the size of an array, two integers representing Polycarp's favorite numbers, and the array itself. For each tuple, it calculates the number of pairs (a, b) in the array such that \(a \mod x\) equals \((-b \mod x + x) \mod x\) and \(a \mod y\) equals \(b \mod y\). It then returns a list of these counts for each test case.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 2 ≤ n ≤ 2⋅10^5 and 1 ≤ x, y ≤ 10^9. arr is a list of n integers such that 1 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: `data` is a list of strings obtained from splitting the input along line breaks, `t` is the first element of `data` converted to an integer, `test_cases` is a list containing tuples of integers where each tuple consists of `n`, `x`, `y`, and `arr`, `n`, `x`, `y` are integers, `arr` is a list of integers, `input` is not yet defined, `idx` is equal to `t * 2 + 1`.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: data is a list of strings obtained from splitting the input along line breaks, t is the first element of data converted to an integer, test_cases is a list containing tuples of integers where each tuple consists of n, x, y, and arr, results is the return value of func_1(test_cases), idx is equal to t * 2 + 1, the console has printed each result in the results list once.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \), followed by \( t \) sets of inputs. Each set includes integers \( n \), \( x \), and \( y \), and a list \( arr \) of \( n \) integers. It calls another function `func_1` with the collected test cases and prints the results returned by `func_1`. The final state of the program includes the console output of the results for all test cases.

