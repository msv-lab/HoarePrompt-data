def main():
    import sys
    input = sys.stdin.read
    data = input().strip()
    r, s, p = map(int, data.split())
    
    dp = [[[0.0 for _ in range(p+1)] for _ in range(s+1)] for _ in range(r+1)]
    
    dp[r][s][p] = 1.0
    
    for i in range(r, -1, -1):
        for j in range(s, -1, -1):
            for k in range(p, -1, -1):
                sum_ = i*j + j*k + k*i
                if i > 0 and j > 0:
                    dp[i-1][j][k] += dp[i][j][k] * (i * j) / sum_
                if j > 0 and k > 0:
                    dp[i][j-1][k] += dp[i][j][k] * (j * k) / sum_
                if k > 0 and i > 0:
                    dp[i][j][k-1] += dp[i][j][k] * (k * i) / sum_
    
    prob_rock = sum(dp[i][0][0] for i in range(r+1))
    prob_scissor = sum(dp[0][j][0] for j in range(s+1))
    prob_paper = sum(dp[0][0][k] for k in range(p+1))
    
    print(f"{prob_rock:.12f} {prob_scissor:.12f} {prob_paper:.12f}")

if __name__ == "__main__":
    main()
