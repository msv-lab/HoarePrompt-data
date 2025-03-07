#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n is an integer representing the number of cards each player receives, where 1 ≤ n ≤ 2 · 10^5. a_1, a_2, ..., a_n are integers representing the numbers on the cards in your hand, where 1 ≤ a_i ≤ n, and each integer from 1 to n appears at most twice in the sequence a_1, a_2, ..., a_n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: `t` is at least 1, the input file has been fully processed, `line` is the last line of input data for the last test case, `elements` is a list of substrings from `line` split by whitespace.
#Overall this is what the function does:The function `func` reads from an input source (likely stdin or a file), processing every other line starting from the third line. Each processed line represents a test case containing a sequence of integers (card numbers). For each test case, the function calculates the sum of the integer division of the count of each unique card number by 3, and prints this sum. After processing all test cases, the input source is fully read, and the function has printed a result for each test case. The function does not return any value.

