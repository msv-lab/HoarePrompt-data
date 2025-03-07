#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i is a list of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, where 0 ≤ p_i[0] + p_i[1] + p_i[2] + p_i[3] ≤ 200.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: the result of the computation for each test case (an integer for each test case)
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads four integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. It then computes a result based on a specific formula involving these counts and prints the result for each test case. The final state of the program includes the printed results for all test cases.

