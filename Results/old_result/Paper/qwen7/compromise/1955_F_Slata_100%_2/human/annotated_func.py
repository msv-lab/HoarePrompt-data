#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200), representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: Output State: The sum of the floor division of each of the four integers \(a\), \(b\), \(c\), and \(d\) by 2, plus 1 if the sum of their modulo 2 values equals 3. This process is repeated for each test case provided by the input.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each test case, it calculates the sum of the floor division of each count by 2, plus 1 if the sum of the modulo 2 values of these counts equals 3. The function outputs this calculated value for each test case.

