#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n is an integer representing the number of cards each player receives, where 1 ≤ n ≤ 2 × 10^5. a_1, a_2, ..., a_n are integers representing the numbers on the cards in your hand, where 1 ≤ a_i ≤ n, and each integer from 1 to n appears at most twice in the sequence. The sum of n over all test cases does not exceed 2 × 10^5.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: `t` is at least 1, the input file has at least `2 * t + 1` lines, and for each test case, the loop has processed the corresponding line, splitting it into `elements` and printing the result of the computation.
#Overall this is what the function does:The function reads from standard input, processing every other line starting from the third line. Each processed line represents a list of integers (cards). The function counts the occurrences of each unique integer in the list, divides the count by 3 (using integer division), and sums these values. The result is printed for each line. The function does not return any value; it only prints the computed results. The function processes multiple test cases, where each test case is defined by a line of input containing a list of integers. The final state of the program is that the input has been fully processed, and the results have been printed for each test case.

