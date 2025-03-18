#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: a series of lines, each containing the computed value for each test case (where the value is computed as described above)
#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence. For each test case, it computes a value based on these counts using a specific formula and prints the result. After processing all test cases, the function concludes with no return value.

