#State of the program right berfore the function call: Each test case contains two positive integers n and k (1 ≤ n, k ≤ 10^{18}) — the number of coins Alice has and the number of jewels Bob wants Alice to have bought at the end. There are t (1 ≤ t ≤ 1000) such test cases.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        if n == k:
            print('YES')
            print(1)
            print(1)
        elif n + 2 > k * 2:
            print('YES')
            print(2)
            print(n - k + 1, end=' ')
            print(1)
        else:
            print('NO')
        
    #State: The output state consists of the results of t test cases, each either printing 'YES' followed by two integers or 'NO'. The values of t, n, and k from the initial state are unchanged except that they have been processed through the loop. The state of other variables not mentioned in the loop remains the same.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers `n` (coins Alice has) and `k` (jewels Bob wants). For each test case, it determines if Alice can buy exactly `k` jewels with her `n` coins under specific conditions and prints 'YES' followed by two integers if possible, otherwise prints 'NO'.

