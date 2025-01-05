MOD = 10**9 + 7

def solve():
    n = int(input())

    if(n<=1):
        print("NO")
    else:   
        print("YES")
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i = 0
        res = ""
        while n>0:
            if n>=2:
                res += letter[i%26] * 2
                n-=2
            else:
                res += letter[i%26]
                n-=1
            i+=1
        print(res)
            
def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()