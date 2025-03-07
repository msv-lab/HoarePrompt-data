#State of the program right berfore the function call: Each test case consists of four integers p1, p2, p3, and p4 (0 ≤ p1, p2, p3, p4 ≤ 200) representing the number of ones, twos, threes, and fours in the sequence, respectively. The function will receive multiple test cases, with the number of test cases t (1 ≤ t ≤ 10^4) provided initially.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: The result for each test case, where the result is the integer division of the calculated sum by 3, with each result on a new line
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours. For each test case, it calculates a specific sum based on these counts and outputs the integer division of this sum by 3, with each result on a new line.

