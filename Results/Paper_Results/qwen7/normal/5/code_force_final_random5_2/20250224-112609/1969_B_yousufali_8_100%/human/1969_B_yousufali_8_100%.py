def solve():
    s = input()
    n = 0
    ans = 0
    
    for i in range(len(s)):
        if s[i] == '1':
            n+=1
        if s[i] == '0' and n!=0:
            ans += n+1
    
    print(ans)
 
def main():
    t = int(input())
    for _ in range(t):
        solve()
 
if __name__ == "__main__":
    main()