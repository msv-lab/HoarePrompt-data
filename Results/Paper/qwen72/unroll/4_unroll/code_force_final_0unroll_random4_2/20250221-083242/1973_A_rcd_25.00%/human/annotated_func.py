#State of the program right berfore the function call: p_1, p_2, and p_3 are non-negative integers such that 0 <= p_1 <= p_2 <= p_3 <= 30, representing the scores of the three players after all games have been played.
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
            low, high = min(p3 - p1, p3 - p2), max(p3 - p1, p3 - p2)
            cur = low
            while high >= cur:
                if p1 - cur <= p2 - (p3 - cur):
                    print(p1 - cur + p3)
                    break
                else:
                    cur += 1
            else:
                print(p3)
        
    #State: The values of p_1, p_2, and p_3 remain unchanged, and t is reduced by the number of iterations the loop has executed.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads three non-negative integers `p1`, `p2`, and `p3` from the input, representing the scores of three players, with the constraint that 0 <= p1 <= p2 <= p3 <= 30. The function then checks the following conditions for each test case:
- If the sum of the scores is odd, it prints `-1`.
- If the highest score `p3` is greater than or equal to the sum of the other two scores `p1 + p2`, it prints `p1 + p2`.
- Otherwise, it calculates a value that satisfies certain conditions and prints either `p1 - cur + p3` or `p3`, where `cur` is a calculated value that ensures the conditions are met. The function does not modify the input scores `p1`, `p2`, and `p3`, and `t` is reduced by the number of test cases processed.

