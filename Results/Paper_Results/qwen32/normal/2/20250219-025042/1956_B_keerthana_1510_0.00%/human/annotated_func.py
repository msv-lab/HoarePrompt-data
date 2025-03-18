#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n, and each integer from 1 through n appears in the list a at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: All test cases have been processed, and the results have been printed. The variable `line` will hold the last processed line, and `elements` will hold the last processed list of string elements.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it calculates and prints the sum of the integer divisions of the count of each unique element in the list by 3.

