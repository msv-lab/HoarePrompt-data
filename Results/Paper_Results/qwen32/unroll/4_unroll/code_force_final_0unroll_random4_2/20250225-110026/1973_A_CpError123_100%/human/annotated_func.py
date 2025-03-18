#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players, sorted in non-decreasing order. The number of test cases t satisfies 1 ≤ t ≤ 500.
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
        
    #State: A series of printed values for each test case, where each value is either `-1` (if the sum of the scores is odd) or the minimum of half the sum of the scores and the sum of the two lower scores (if the sum is even).
#Overall this is what the function does:The function processes multiple test cases, each consisting of three sorted integer scores. For each test case, it checks if the sum of the scores is odd. If it is, the function outputs `-1`. If the sum is even, it calculates two values: half of the total sum and the sum of the two lower scores, then outputs the smaller of these two values.

