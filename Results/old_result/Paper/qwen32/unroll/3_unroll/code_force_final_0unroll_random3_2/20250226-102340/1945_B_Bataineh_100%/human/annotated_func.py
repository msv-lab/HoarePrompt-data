#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is unchanged; `a`, `b`, and `m` are the values from the last iteration of the loop.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints a result based on the relationships between these integers. The result is determined by how `m` compares to `a` and `b`, and involves integer division operations.

