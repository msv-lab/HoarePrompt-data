#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: t lines of output, each line containing the value of A + B, where A = int(m / a) + 1 and B = int(m / b) + 1 for the corresponding input values of a, b, and m.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`. It calculates `A` as `int(m / a) + 1` and `B` as `int(m / b) + 1`, then prints the sum `A + B`.

