#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200), representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: Output State: The output state after the loop executes all the iterations is the sum of `a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3)`, calculated for each input provided during the loop's iterations.
    #
    #Natural Language Description: After the loop has completed all its iterations, the output state is the total sum of half the values of `a`, `b`, `c`, and `d` (using integer division), plus one if the sum of the odd parts of `a`, `b`, and `c` equals 3. This process is repeated for each set of inputs provided during the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence. For each test case, it calculates the total count of these numbers by taking half of each count (using integer division) and adding one if the sum of the odd parts of the counts of 1s, 2s, and 3s equals 3. The function outputs this calculation for each test case.

