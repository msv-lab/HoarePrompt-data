#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case where 1 ≤ n ≤ 3 \cdot 10^5 and 0 ≤ k ≤ n, and each of the k moves is represented by two integers r_i and c_i, ensuring that the moves are valid and do not result in rooks attacking each other.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n, k = list(map(int, input().split(' ')))
        
        num = 0
        
        for i in range(k):
            c, r = list(map(int, input().split(' ')))
            if c == r:
                num += 1
            else:
                num += 2
        
        m = n - num
        
        if m == 0:
            print(0)
        elif m == 1:
            print(1)
        else:
            dp = [(0) for i in range(m + 1)]
            dp[1] = 1
            dp[2] = 3
            for i in range(3, m + 1):
                dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10 ** 9 + 7)
            print(dp[m])
        
    #State: t is 0, and the loop has executed all the iterations.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`, representing the size of a chessboard and the number of rooks, respectively. It then reads `k` pairs of integers, each representing a move of a rook on the chessboard. The function calculates the number of ways to place the remaining rooks on the chessboard such that no two rooks attack each other, and prints the result for each test case. After processing all test cases, the function terminates with `t` being 0.

