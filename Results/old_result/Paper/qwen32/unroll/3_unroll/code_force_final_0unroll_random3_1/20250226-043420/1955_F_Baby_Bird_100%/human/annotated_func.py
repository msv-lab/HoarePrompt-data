#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains four integers p1, p2, p3, p4 (0 ≤ p1, p2, p3, p4 ≤ 200) representing the number of ones, twos, threes, and fours in the sequence, respectively.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: - The result of the final calculation for each test case is converted to a string and collected into a list.
    #   - `'\n'.join(...)` joins these strings with newline characters to form the final output string.
    #
    #### Output Explanation:
    #The output of the program is a series of integers, one per line, where each integer represents the calculated value for each test case based on the given formula.
    #
    #### Final Output:
    #Output:
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates a specific value based on these counts and outputs the result for each test case on a new line.

