#State of the program right berfore the function call: Each test case consists of four integers p1, p2, p3, and p4 (0 ≤ p1, p2, p3, p4 ≤ 200) representing the number of ones, twos, threes, and fours in the sequence, respectively. The input starts with an integer t (1 ≤ t ≤ 10^4) indicating the number of test cases.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: result for each test case, separated by newlines
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing counts of ones, twos, threes, and fours. For each test case, it calculates a result based on these counts and prints the result for each test case, separated by newlines.

