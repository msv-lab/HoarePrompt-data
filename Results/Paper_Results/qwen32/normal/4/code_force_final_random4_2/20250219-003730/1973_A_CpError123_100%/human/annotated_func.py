#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players sorted in non-decreasing order. The number of test cases t satisfies 1 ≤ t ≤ 500.
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
        
    #State: t is 0, p_1, p_2, and p_3 are integers such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers representing scores of players sorted in non-decreasing order. For each test case, it calculates and prints either -1 if the sum of the scores is odd, or the minimum of half the total sum of the scores and the sum of the two lower scores.

