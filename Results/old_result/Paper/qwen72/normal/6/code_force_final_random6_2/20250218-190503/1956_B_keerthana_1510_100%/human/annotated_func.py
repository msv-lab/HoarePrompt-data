#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 2 · 10^5, representing the number of cards each player receives. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ n, representing the integers on the cards in your hand. Each integer from 1 to n appears at most twice in the sequence a_1, a_2, ..., a_n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: The file opened by `open(0)` must have at least 2t + 1 lines, `line` is the (2t + 1)-th line of the file.
#Overall this is what the function does:The function `func` processes a file where each test case is represented by a line of space-separated integers. For each test case, it calculates and prints the difference between the total number of integers and the number of unique integers in that line. The function does not accept any parameters and does not return any values. The state of the program after the function concludes is that the file has been read, and the results for each test case have been printed to the console.

