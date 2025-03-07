#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the list of integers a_1, a_2, ..., a_n contains unique integers from 1 to n, each appearing at most twice.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: Output State: The loop continues to read lines from standard input, specifically processing every second line starting from the third line. For each processed line, `elements` is a list of strings obtained by splitting the line on whitespace. The code then prints the sum of counts of each unique item in `elements`, divided by 3, for all unique items in `elements`.
    #
    #This process repeats until there are no more valid lines to process according to the given pattern (every second line starting from the third line). Once all such lines have been processed, the loop terminates.
#Overall this is what the function does:The function processes a series of lines from standard input, specifically every second line starting from the third line. For each processed line, it calculates the sum of counts of each unique item, divided by 3, and prints this value. The function does not return any value but produces output based on the input provided.

