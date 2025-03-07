#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i is a list of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, where 0 ≤ p_i[0] + p_i[1] + p_i[2] + p_i[3] ≤ 200.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: a series of lines, each containing the result of the described calculation for each test case
#Overall this is what the function does:The function processes a series of test cases, where each test case is represented by a line of input containing four space-separated integers. These integers represent the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each test case, the function calculates a specific value based on these counts and prints the result. The final state of the program includes a series of lines, each containing the calculated result for each test case.

