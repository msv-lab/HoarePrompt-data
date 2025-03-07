#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i is a list of four integers (0 <= p_i <= 200) representing the number of ones, twos, threes, and fours in the sequence at the beginning of the game.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: [result1]
    #[result2]
    #...
    #[resultT] (where result1, result2, ..., resultT are the integer results of the sum calculation for each test case, divided by 3 using integer division)
#Overall this is what the function does:The function `func` reads a series of test cases, each defined by a list of four integers representing counts of ones, twos, threes, and fours. For each test case, it calculates a result based on these counts, specifically summing a modified version of these counts and then performing integer division by 3. The function prints the results for each test case, one per line. The function does not return any value; it only prints the results.

