#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players, sorted in non-decreasing order. The number of test cases t is between 1 and 500 inclusive.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: a series of t outputs, each being either -1 or a calculated result based on the scores of the three players.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three sorted scores (p_1, p_2, p_3) of players. For each test case, it calculates and prints either -1 if the sum of the scores is odd, or a calculated result based on the scores if the sum is even.

