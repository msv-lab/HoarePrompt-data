#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, there are four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: the result of the calculation for each test case, separated by newlines (where the result for each test case is the sum of the processed counts divided by 3, formatted as a string)
#Overall this is what the function does:The function processes a series of test cases, each defined by four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each test case, it calculates a specific value based on these counts, divides the sum by 3, and prints the result. The function reads the number of test cases from the first line of input and the counts for each test case from subsequent lines.

