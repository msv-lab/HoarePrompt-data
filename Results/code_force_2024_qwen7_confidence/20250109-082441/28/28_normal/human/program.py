def gcd(x, y):  
    if y == 0:  
        return x  
    return gcd(y, x % y)  
  
def solve():  
    a, b = map(int, input().split())  
    ans = 0  
    for x in range(1, int(a**0.5) + 1):  
        for y in range(1, int(b**0.5) + 1):  
            if gcd(x, y) == 1:  
                cnt = min(a // ((x + y) * x), b // ((x + y) * y))  
                if cnt >= 1:  
                    ans += cnt  
    print(ans)  
  
if __name__ == "__main__":  
    T = int(input())  
    for _ in range(T):  
        solve()