#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i is a list of four integers (0 <= p_i <= 200) representing the number of ones, twos, threes, and fours in the sequence, respectively.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: 4
    #2
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `t` and a list `p_i` of four integers representing counts of ones, twos, threes, and fours. For each test case, it calculates a value based on these counts and prints the result. The function does not return any value; it only prints the results.

