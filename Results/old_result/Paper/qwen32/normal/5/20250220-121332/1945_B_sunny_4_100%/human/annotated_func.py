#State of the program right berfore the function call: Each test case consists of three integers a, b, and m (1 ≤ a, b, m ≤ 10^18) representing the frequency of launching fireworks for the first and second installations, and the visibility duration of each firework, respectively. There are t (1 ≤ t ≤ 10^4) such test cases.
def func():
    """t=int(input())
    for _ in range(t):
        a,b,m=map(int,input().split())
        A=int(m/a)+1
        B=int(m/b)+1
        print(A+B)"""
    t = int(input())
    for qi in range(t):
        a, b, m = [int(x) for x in input().split()]
        
        ans = m // a + m // b + 2
        
        print(ans)
        
    #State: `qi` is `t`, `a`, `b`, and `m` are the values read during the last iteration, and the last computed `ans` is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints the result based on the frequencies of launching fireworks (`a` and `b`) and the visibility duration (`m`).

