#State of the program right berfore the function call: Each test case consists of four integers p1, p2, p3, p4 (0 ≤ p1, p2, p3, p4 ≤ 200) representing the counts of ones, twos, threes, and fours in the sequence, respectively. The first line of input contains an integer t (1 ≤ t ≤ 10^4), which is the number of test cases.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: result1\nresult2\n...\nresultt (where result1, result2, ..., resultt are the calculated values for each of the t test cases)
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads four integers `p1`, `p2`, `p3`, and `p4` representing the counts of ones, twos, threes, and fours in a sequence, respectively. It then calculates and prints a result for each test case based on these counts. The final state of the program is the printed results, one per line, corresponding to each test case.

