#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 1000), and cases is a list of tuples, where each tuple contains two integers n and k such that (2 ≤ n ≤ 10^6) and (1 ≤ k ≤ n). The sum of n over all test cases does not exceed 10^7.
def func_1(t, cases):
    results = []
    sequence = [(2 ** i) for i in range(25)]
    for (n, k) in cases:
        results.append((25, sequence))
        
    #State: `t` is a positive integer (1 ≤ t ≤ 1000), `cases` is a list of tuples, where each tuple contains two integers n and k such that (2 ≤ n ≤ 10^6) and (1 ≤ k ≤ n). The sum of n over all test cases does not exceed 10^7. `results` is a list containing `t` elements, where each element is a tuple (25, sequence). `sequence` is a list containing the powers of 2 from 2^0 to 2^24.
    return results
    #The program returns a list `results` containing `t` elements, where each element is a tuple (25, sequence). The `sequence` list contains the powers of 2 from 2^0 to 2^24.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list of tuples `cases`. It returns a list `results` containing `t` elements, where each element is a tuple `(25, sequence)`. The `sequence` list contains the powers of 2 from 2^0 to 2^24. The function does not modify the input parameters `t` or `cases`.

