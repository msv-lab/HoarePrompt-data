#State of the program right berfore the function call: The function should take two parameters: a list of integers `numbers` representing the numbers on the cards, and an integer `k` (2 ≤ k ≤ 100) representing the number of cards to be exchanged in each operation. The list `numbers` should have a length `n` (1 ≤ n ≤ 100) and each element `c_i` in `numbers` should be an integer (1 ≤ c_i ≤ 100).
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: The variable `t` is decremented by the number of iterations the loop has executed. The variables `n`, `k`, and `l` are updated in each iteration based on the input provided during that iteration. The loop prints `k - 1` for each iteration. The list `numbers` and the integer `k` from the initial state remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. Instead, it reads input from the user multiple times. It first reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`, and a list of integers `l`. The function then prints `k - 1` for each test case. The initial variables `numbers` and `k` mentioned in the annotations are not used or modified by the function. After the function concludes, the variable `t` is exhausted (decremented to 0), and the variables `n`, `k`, and `l` are updated for each iteration based on the input provided.

