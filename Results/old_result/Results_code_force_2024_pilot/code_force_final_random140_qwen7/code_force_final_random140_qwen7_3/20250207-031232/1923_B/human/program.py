def monster_attack():
    try:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = [0] * (n + 1)
        
        for i in range(n):
            x = int(input())
            b[abs(x)] += a[i]
        
        r = 0
        for i in range(1, n + 1):
            r += k
            if r < b[i]:
                print("NO")
                return
            r -= b[i]
        
        print("YES")
    except ValueError:
        print("Invalid input format")
 
def main():
    try:
        t = int(input())
        for _ in range(t):
            monster_attack()
    except ValueError:
        print("Invalid input format")
 
if __name__ == "__main__":
    main()