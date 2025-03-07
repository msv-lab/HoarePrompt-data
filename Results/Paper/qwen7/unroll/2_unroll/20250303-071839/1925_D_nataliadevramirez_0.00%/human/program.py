MOD = 10**9 + 7
 
def calculate_expected_value(n, m, k, friendships):
    result = 0
 
    for i in range(m):
        a, b, f = friendships[i]
        result += f * (k * (k + 1) // 2) % MOD
 
    return result % MOD
 
def main():
    t = int(input())
    
    for _ in range(t):
        n, m, k = map(int, input().split())
        friendships = [list(map(int, input().split())) for _ in range(m)]
 
        result = calculate_expected_value(n, m, k, friendships)
        print(result)
 
if __name__ == "__main__":
    main()