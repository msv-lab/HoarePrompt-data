#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains three integers a, b, and m such that 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: A series of printed values, each determined by the formula `mn // a + mn // b + 1` if `m % a == 0 and m % b == 0 and a != 1 and b != 1`; otherwise, `mn // a + mn // b`, where `mn = min(a, b) + m` for each set of `a`, `b`, and `m` read from the input.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`. It then computes and prints a value based on these inputs. Specifically, it calculates `mn` as the minimum of `a` and `b` plus `m`. If `m` is divisible by both `a` and `b` and neither `a` nor `b` is 1, it prints `mn // a + mn // b + 1`. Otherwise, it prints `mn // a + mn // b`.

