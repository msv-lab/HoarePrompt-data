#State of the program right berfore the function call: Each test case consists of four integers p_i (0 ≤ p_i ≤ 200) representing the counts of ones, twos, threes, and fours in the sequence. The number of test cases t satisfies 1 ≤ t ≤ 10^4.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: p_i (counts of ones, twos, threes, and fours remain unchanged)
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours. For each test case, it calculates and prints a value based on these counts. The counts themselves remain unchanged after processing each test case.

