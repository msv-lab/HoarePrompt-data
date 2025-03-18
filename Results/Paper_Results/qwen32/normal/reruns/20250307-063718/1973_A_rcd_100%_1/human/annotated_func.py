#State of the program right berfore the function call: There are multiple test cases, where each test case consists of three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of three players after a series of chess games, with p_1, p_2, and p_3 being non-decreasing. The number of test cases t satisfies 1 ≤ t ≤ 500.
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
        
    #State: The loop has executed `t` times, and for each set of input values `p1`, `p2`, and `p3`, the program has printed the appropriate result based on the given conditions.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of three integers `p1`, `p2`, and `p3` representing the scores of three players in non-decreasing order. For each test case, it determines and prints a value based on the scores, ensuring that the sum of the scores is even. If the sum is odd, it prints `-1`. If `p3` is greater than or equal to the sum of `p1` and `p2`, it prints the sum of `p1` and `p2`. Otherwise, it finds the maximum possible value of `p1 - x + p3` such that `p1 - x <= p2 - (p3 - x)` and prints this value. If no such `x` exists, it prints `p3`.

