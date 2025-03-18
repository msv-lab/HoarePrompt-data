#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. Each of the following t lines contains three integers p_1, p_2, and p_3 such that 0 <= p_1 <= p_2 <= p_3 <= 30.
def func():
    t = int(input())
    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        
        if (p1 + p2 + p3) % 2 != 0:
            print(-1)
            continue
        
        if p3 >= p1 + p2:
            print(p1 + p2)
        else:
            x = 0
            y = p3
            while y >= x:
                if p1 - x <= p2 - y:
                    print(p1 - x + p3)
                    break
                else:
                    x += 1
                    y -= 1
            else:
                print(p3)
        
    #State: a series of printed values for each of the `t` iterations, based on the conditions described above.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `p_1`, `p_2`, and `p_3`. For each test case, it prints a value based on specific conditions: if the sum of `p_1`, `p_2`, and `p_3` is odd, it prints `-1`. Otherwise, it calculates and prints a value that is the maximum possible sum of two numbers from the set `{p_1, p_2, p_3}` under certain constraints.

