#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200), representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, respectively.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: Output State: The sum of the results from each iteration where `a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3)` is calculated for the given inputs `a`, `b`, `c`, and `d` for each test case. This sum represents the total number of pairs (or nearly pairs) that can be formed from the counts of 1s, 2s, 3s, and 4s in each test case.
#Overall this is what the function does:The function reads multiple test cases, each consisting of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s. For each test case, it calculates the total number of pairs (or nearly pairs) that can be formed from these counts and prints the result. After processing all test cases, it outputs the sum of these results.

