#State of the program right berfore the function call: fountain is a tuple of two integers (r, c) representing the coordinates of a fountain on the field, n and m are integers representing the dimensions of the field such that 2 <= n, m <= 10^9.
def func_1(fountain, n, m):
    r, c = fountain
    diagonal_distance = abs(r + c - (n + 1))
    return max(diagonal_distance // 2, 0)
    #`The program returns max(abs(r + c - (n + 1)) // 2, 0)`
#Overall this is what the function does:The function `func_1` accepts a tuple `fountain` containing the coordinates `(r, c)` of a fountain on a field, along with the dimensions `n` and `m` of the field. It calculates the maximum of half the absolute difference between the sum of the fountain's coordinates and the sum of the field dimensions incremented by one (`abs(r + c - (n + 1)) // 2`), and zero. The function returns this calculated value. The function handles edge cases where the result of the calculation could be negative by ensuring the returned value is at least zero.

#State of the program right berfore the function call: t is a positive integer indicating the number of test cases; n, m, and k are positive integers such that 2 ≤ n, m ≤ 10^9 and 2 ≤ k ≤ 2 * 10^5; for each test case, r and c are positive integers representing the row and column of a fountain, with 1 ≤ r ≤ n and 1 ≤ c ≤ m, and all fountain positions are unique and none of them is (n, 1).
def func_2():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        m = int(data[index + 1])
        
        k = int(data[index + 2])
        
        index += 3
        
        alpha = (n * m + 1) // 2
        
        additional_areas = []
        
        for __ in range(k):
            r = int(data[index])
            c = int(data[index + 1])
            index += 2
            additional_areas.append(func_1((r, c), n, m))
        
        results.append((alpha, additional_areas))
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `index` is `2 + t * 2 + 3`, `results` is a list of tuples, each tuple contains `alpha` and `additional_areas`; `alpha` is \((n * m + 1) // 2\) for each tuple, where `n` and `m` are the integers corresponding to the first two elements of the `data` list for each tuple; `additional_areas` is a list containing the results of `func_1((r, c), n, m)` for each fountain position \((r, c)\) provided in the `data` list for each tuple; `r` and `c` are the integers corresponding to the fountain positions in the `data` list for each tuple.
    for result in results:
        alpha, additional_areas = result
        
        print(alpha)
        
        print(' '.join(map(str, additional_areas)))
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `index` is \(2 + (t + |results| - 1) \times 2 + 3\), `results` is a list of tuples, `alpha` is the first element of the last tuple in `results`, `additional_areas` is the second element of the last tuple in `results`, and `alpha` is printed for each tuple in `results`.
#Overall this is what the function does:The function processes multiple test cases, each involving a grid of dimensions \(n \times m\). For each test case, it calculates an initial value \(\alpha\) which is \((n \times m + 1) // 2\). It also computes the area added by \(k\) fountains located at specific positions \((r, c)\) within the grid. For each fountain, it calls another function `func_1` to determine the additional area contributed by that fountain. The results for each test case are stored in a list of tuples, where each tuple contains \(\alpha\) and a list of the additional areas contributed by the fountains. Finally, the function prints \(\alpha\) and the list of additional areas for each test case. The function handles edge cases such as the unique positions of the fountains and the constraints on \(n\), \(m\), and \(k\). However, it does not account for the possibility of invalid input (e.g., non-positive integers for \(n\), \(m\), \(k\), \(r\), and \(c\)).

