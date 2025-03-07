#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n, and each integer from 1 to n appears at most 2 times in the list. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: The values of t, n, and a remain unchanged. The loop iterates through the input lines, processing every third line starting from the third line. For each processed line, it calculates and prints the difference between the number of tokens in the line and the number of unique tokens. The state of t, n, and a is not affected by the loop.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads input from standard input, processes every third line starting from the third line, and for each processed line, it calculates and prints the difference between the number of tokens in the line and the number of unique tokens. The function does not modify the state of any external variables or parameters.

