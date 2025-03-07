#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players, sorted in non-decreasing order. The first line of the input contains an integer t (1 ≤ t ≤ 500) indicating the number of test cases.
def func():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if (a + b + c) % 2 != 0:
            print(-1)
            continue
        
        x = (a + b + c) // 2
        
        y = a + b
        
        print(min(x, y))
        
    #State: t is an integer representing the number of test cases; p_1, p_2, and p_3 are each integers representing the scores of the three players, sorted in non-decreasing order.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three sorted scores of players, and for each test case, it outputs either the minimum of half the total score or the sum of the first two scores, provided the total score is even; otherwise, it outputs -1.

