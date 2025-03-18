#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players, sorted in non-decreasing order. The first line of the input contains an integer t (1 ≤ t ≤ 500) representing the number of test cases.
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
        
    #State: A sequence of outputs for each test case, where each output is either `-1`, `p1 + p2`, or a value derived from the while loop logic as described.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three sorted integer scores representing the scores of three players. For each test case, it determines and prints a value based on the scores: `-1` if the sum of the scores is odd, `p1 + p2` if the highest score is at least the sum of the other two scores, or a calculated value derived from balancing the scores otherwise.

