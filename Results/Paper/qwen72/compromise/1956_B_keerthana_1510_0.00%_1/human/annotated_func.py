#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ n. Each integer from 1 to n appears at most twice in the list a. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: The variable `t` remains unchanged, the variable `n` remains unchanged, and the list `a` remains unchanged. The loop processes the input and prints the sum of the counts of each unique element in the list `a` divided by 3, for each test case.
#Overall this is what the function does:The function `func` reads input from standard input, processes each test case (skipping the first and every second line), and prints the sum of the counts of each unique element in the list of elements from the line, divided by 3. The function does not accept any parameters and does not return any values. The variables `t`, `n`, and `a` mentioned in the annotations are not directly used or modified by the function.

