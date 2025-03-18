#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case consists of four integers p_i (0 ≤ p_i ≤ 200) representing the number of ones, twos, threes, and fours in the sequence, respectively.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: result1\nresult2\n...\nresultt (where each resulti is the maximum number of groups of three that can be formed from the counts of ones, twos, threes, and fours in the ith test case, considering the special rule for unpaired elements)
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours. It calculates and prints the maximum number of groups of three that can be formed from these counts, applying a special rule for unpaired elements.

