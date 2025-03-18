#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, there are four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: the result of the division of the summation by 3 for each test case, separated by newlines
#Overall this is what the function does:The function reads a series of test cases, each defined by four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each test case, it calculates a value based on these counts using a specific formula, then divides the result by 3 and prints the outcome. The function processes up to 10,000 test cases.

