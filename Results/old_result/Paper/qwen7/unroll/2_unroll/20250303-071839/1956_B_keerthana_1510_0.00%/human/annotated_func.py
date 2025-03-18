#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and for each test case, a list of n integers a_1, a_2, ..., a_n is given where 1 ≤ a_i ≤ n and each integer from 1 through n appears at most twice in the list.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and for each test case, a list of n integers a_1, a_2, ..., a_n is given where 1 ≤ a_i ≤ n and each integer from 1 through n appears at most twice in the list. After executing the loop, for each test case, the output is the sum of counts of unique elements in the list divided by 3, printed for every second line starting from the third line of input.
    #
    #This means that for each test case, the loop processes every second line (starting from the third line) of the input, calculates the sum of counts of each unique element in the line divided by 3, and prints this value. The initial and final states of `t` and `n` remain unchanged, but the output will consist of these calculated sums for each relevant line of input.
#Overall this is what the function does:The function processes input data consisting of multiple test cases. For each test case, it reads a line of input, splits it into elements, and calculates the sum of counts of each unique element in the line, dividing this sum by 3. This calculation is performed for every second line starting from the third line of input. The function outputs these calculated values for each relevant line of input. The initial values of `t` and `n` remain unchanged, but the output consists of the calculated sums for each test case.

