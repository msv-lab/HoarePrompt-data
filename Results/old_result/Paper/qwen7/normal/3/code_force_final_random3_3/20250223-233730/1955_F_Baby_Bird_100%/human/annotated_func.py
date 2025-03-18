#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200), representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, respectively.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: the integer part of the sum of the computed values for each test case divided by 3
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence. For each test case, it calculates the sum of specific formulas applied to these counts, divides the result by 3, and outputs the integer part of this division. The function then prints the calculated value for each test case on a new line.

