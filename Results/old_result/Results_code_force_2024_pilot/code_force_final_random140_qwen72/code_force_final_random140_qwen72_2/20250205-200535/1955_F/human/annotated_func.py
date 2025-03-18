#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i are integers such that 0 <= p_i <= 200, representing the counts of the numbers 1, 2, 3, and 4 in the sequence.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 3 == 3))
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `p_i` are integers such that 0 <= p_i <= 200, `i` is `int(input()) - 1`, and `a`, `b`, `c`, and `d` are integers provided by the user.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where 1 <= t <= 10^4. For each test case, it reads four integers `a`, `b`, `c`, and `d` (0 <= p_i <= 200), representing counts of the numbers 1, 2, 3, and 4 in a sequence. It then calculates and prints a value based on these inputs, which is the sum of the integer divisions of `a`, `b`, `c`, and `d` by 2, plus 1 if the sum of their remainders when divided by 2 and 3 equals 3. After processing all test cases, the function completes without returning any value.

