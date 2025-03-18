#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) indicating the number of test cases. Each of the following t lines contains four integers p_i (0 ≤ p_i ≤ 200) representing the count of ones, twos, threes, and fours in the sequence for each test case.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: The output will consist of `t` lines, each containing the calculated value `a // 2 + b // 2 + c // 2 + int(a % 2 + b % 2 + c % 2 == 3)` for the corresponding test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing counts of ones, twos, threes, and fours. For each test case, it calculates a value based on these counts and prints the result. The final state of the program is the output of these calculated values, one per test case.

