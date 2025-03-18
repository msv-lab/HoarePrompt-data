#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i are integers such that 0 <= p_i <= 200, representing the number of ones, twos, threes, and fours in the sequence, respectively.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: result (where result is the integer division of the sum of the calculated values by 3 for each test case)
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads four integers `p_i` representing the number of ones, twos, threes, and fours in a sequence. It then calculates and prints the integer division of the sum of a specific transformation of these values by 3. The function does not return any value but prints the result for each test case. If any input is out of the specified ranges (1 <= t <= 10^4 and 0 <= p_i <= 200), the function does not handle these cases and may produce unexpected results or errors.

