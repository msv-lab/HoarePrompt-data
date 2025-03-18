#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and each of the four integers p_i in each test case is an integer where 0 ≤ p_i ≤ 200.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 3 == 3))
        
    #State: `i` is `t-1`, `a`, `b`, `c`, and `d` are integers provided by the user and each is greater than or equal to 0.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where `1 ≤ t ≤ 10^4`. For each test case, it reads four integers `a`, `b`, `c`, and `d` (where `0 ≤ p_i ≤ 200`). It then calculates and prints the sum of the integer division of each of these numbers by 2, plus 1 if the sum of their remainders when divided by 2 and 3 respectively equals 3. After processing all test cases, the function completes without returning any value.

