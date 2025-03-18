#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: `i` is 3, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `a` is the first integer input, `b` is the second integer input, `c` is the third integer input, `d` is the fourth integer input, the values of `a`, `b`, `c`, and `d` are integers obtained from the input split by spaces.
#Overall this is what the function does:The function processes a series of test cases, each consisting of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each test case, it calculates and prints the total count of these numbers, adjusted based on certain conditions involving the remainders when divided by 2. The function does not return any value but prints the result for each test case.

