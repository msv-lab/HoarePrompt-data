#State of the program right berfore the function call: Each test case consists of four integers p1, p2, p3, and p4 (0 ≤ p1, p2, p3, p4 ≤ 200) representing the number of ones, twos, threes, and fours in the sequence, respectively. The total number of test cases, t, satisfies 1 ≤ t ≤ 10^4.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: p1, p2, p3, p4
#Overall this is what the function does:The function reads multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates and prints a value based on these counts, which seems to represent a specific derived count related to the input numbers.

