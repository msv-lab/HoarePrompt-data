#State of the program right berfore the function call: test_cases is a list of tuples, where each tuple contains four elements: n (an integer representing the size of the array), x and y (two integers representing Polycarp's favorite integers), and arr (a list of integers representing the elements of the array). Each element in arr is an integer such that 1 <= a_i <= 10^9.
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
        
    #State: `test_cases` is an empty list, `n` is undefined, `x` is undefined, `y` is undefined, `arr` is an empty list, `freq` is an empty dictionary, `count` is 0, and `results` is a list containing the sum of counts from each iteration of the loop.
    return results
    #The program returns an empty list for `results` since no iterations were performed and `results` was initialized as an empty list.
#Overall this is what the function does:The function accepts a parameter `test_cases`, which is a list of tuples. Each tuple contains four elements: `n` (an integer representing the size of the array), `x` and `y` (two integers representing Polycarp's favorite integers), and `arr` (a list of integers representing the elements of the array). The function processes each tuple in `test_cases`, calculates the frequency of certain pairs derived from elements in `arr`, and appends a count to the `results` list. However, since no iterations are performed (as indicated by the return postconditions), the function returns an empty list.

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
        
    #State: Output State: `test_cases` is a list containing five tuples \[(n, x, y, arr)\], `idx` is `idx + 10`, `t` is `t - 3`, where each tuple contains integers \(n\), \(x\), and \(y\) followed by a list of integers `arr` converted from `data[idx + 1].split()`. The loop has executed all its iterations, and `t` has been decremented by the total number of iterations, which is 5 in this case.
    results = func_1(test_cases)
    for result in results:
        print(result)
        
    #State: The loop will have executed 5 times since there are 5 tuples in `test_cases`. The `results` list will be fully iterated, and `result` will be the last element in the `results` list after the loop completes.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer \( t \), followed by \( t \) sets of three integers \( n \), \( x \), and \( y \), and a list of \( n \) integers \( arr \). It then processes these test cases using another function `func_1`, collects the results, and prints them. The function effectively transforms raw input data into processed output data by handling up to 5 test cases.

