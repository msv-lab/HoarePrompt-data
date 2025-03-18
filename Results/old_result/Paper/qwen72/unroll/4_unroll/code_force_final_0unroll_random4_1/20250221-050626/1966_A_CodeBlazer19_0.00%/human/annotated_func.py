#State of the program right berfore the function call: The function should take two parameters: a list of integers `cards` (1 <= len(cards) <= 100) representing the numbers on the cards, and an integer `k` (2 <= k <= 100) representing the number of cards to exchange during each operation. The function should be called within a loop that processes multiple test cases, where the number of test cases `t` is an integer (1 <= t <= 500).
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: `t` is an input integer (1 <= t <= 500), `cards` is a list of integers (1 <= len(cards) <= 100), `k` is an integer (2 <= k <= 100). The loop prints `k - 1` for each iteration, but the values of `t`, `cards`, and `k` remain unchanged after the loop finishes.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `n` is the length of a list of integers and `k` is the number of cards to exchange. It then reads a list of `n` integers from the input. The function prints `k - 1` for each test case. The function does not modify the input values or the state of the program beyond the printed output.

