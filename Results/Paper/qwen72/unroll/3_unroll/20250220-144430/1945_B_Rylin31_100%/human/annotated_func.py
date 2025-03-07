#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: t test cases have been processed, and for each test case, the output is the sum of the integer division of m by a, the integer division of m by b, and 2. The values of a, b, and m are not retained after each iteration.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer such that 1 ≤ t ≤ 10^4. For each test case, it reads three integers `a`, `b`, and `m` such that 1 ≤ a, b, m ≤ 10^18, and prints the sum of the integer division of `m` by `a`, the integer division of `m` by `b`, and 2. The values of `a`, `b`, and `m` are not retained after each iteration. After processing all test cases, the function concludes without returning any value.

