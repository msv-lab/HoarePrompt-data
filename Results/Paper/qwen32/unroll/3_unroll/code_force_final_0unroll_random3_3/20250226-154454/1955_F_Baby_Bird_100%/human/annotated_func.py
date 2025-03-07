#State of the program right berfore the function call: Each test case consists of four integers p1, p2, p3, and p4 (0 ≤ p1, p2, p3, p4 ≤ 200) representing the counts of ones, twos, threes, and fours in the sequence, respectively. The input starts with an integer t (1 ≤ t ≤ 10^4) denoting the number of test cases.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: result1\nresult2\n...\nresultt (where each resulti is the calculated value for the i-th test case)
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates a specific value based on these counts and prints the results, one per line.

