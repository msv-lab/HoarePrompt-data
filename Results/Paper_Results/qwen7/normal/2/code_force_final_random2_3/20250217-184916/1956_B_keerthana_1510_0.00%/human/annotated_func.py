#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and the list a contains n integers where each integer is in the range 1 to n, inclusive, and appears at most twice. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: Output State: The loop has processed all lines of input as per the given condition (taking every second line starting from the third line). For each valid `line`, `elements` is a list of strings obtained by splitting that line. The code inside the loop calculates the sum of counts of each unique item in `elements` divided by 3 and prints it. This process is repeated for all lines that meet the criteria until there are no more lines left to process.
    #
    #In simpler terms, after all iterations of the loop, the output will consist of the sum of counts of each unique item in every valid line (starting from the third line and taking every second line) divided by 3, printed for each line.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads an integer `t` (1 ≤ t ≤ 10^4), an integer `n` (1 ≤ n ≤ 2 ⋅ 10^5), and a list `a` containing `n` integers (each in the range 1 to n, inclusive, and appearing at most twice). It then prints the sum of counts of each unique item in every valid line (starting from the third line and taking every second line) divided by 3 for each test case. The function does not return any value but produces output based on the input provided.

