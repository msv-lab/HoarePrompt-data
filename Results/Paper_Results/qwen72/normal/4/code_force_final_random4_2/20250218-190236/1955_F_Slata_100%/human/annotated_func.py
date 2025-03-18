#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i is a list of four integers (0 <= p_i <= 200) representing the number of ones, twos, threes, and fours in the sequence.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `p_i` is a list of four integers (0 <= p_i <= 200) representing the number of ones, twos, threes, and fours in the sequence, `i` is `t-1`, `a`, `b`, `c`, and `d` are the input integers, each greater than 0, and the loop has executed `t` times.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case is defined by four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, the function calculates and prints a value which is the sum of half the counts of each integer (rounded down) plus 1 if exactly three of the counts are odd. The function does not return any value; it only prints the results for each test case. After the function concludes, the loop has executed `t` times, where `t` is the number of test cases, and the final state includes the printed results for all test cases.

