#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case contains four integers p_i (0 ≤ p_i ≤ 200) representing the number of ones, twos, threes, and fours in the sequence, respectively.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: a series of integers, each representing the result of the computation for one test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates and prints a result based on these counts. The result is the sum of half the counts of each number (rounded down) plus one if the sum of the remainders when each count is divided by two equals three.

