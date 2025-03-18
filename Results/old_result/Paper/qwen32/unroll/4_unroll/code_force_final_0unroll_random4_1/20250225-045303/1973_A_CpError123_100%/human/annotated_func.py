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
        
    #State: [output values for each test case]
#Overall this is what the function does:The function processes multiple test cases, each consisting of three sorted scores (in non-decreasing order) for three players. For each test case, it checks if the sum of the scores is even. If the sum is odd, it outputs -1. If the sum is even, it calculates half of the total score and compares it with the sum of the first two scores, outputting the smaller of the two values.

