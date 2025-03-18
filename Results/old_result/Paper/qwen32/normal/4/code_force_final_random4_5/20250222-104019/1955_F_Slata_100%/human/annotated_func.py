#State of the program right berfore the function call: Each test case consists of four integers p_i (0 ≤ p_i ≤ 200) representing the counts of ones, twos, threes, and fours in the sequence, respectively. The number of test cases t satisfies 1 ≤ t ≤ 10^4.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: The sum of the computed values from each iteration, where each computed value is determined by the formula `a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3)` for each set of input values `a`, `b`, `c`, and `d`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing counts of ones, twos, threes, and fours. For each test case, it calculates a value based on the formula `a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3)` and prints the result.

