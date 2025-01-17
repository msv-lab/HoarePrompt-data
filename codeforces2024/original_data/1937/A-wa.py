
gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
def takeintinput():
    arr = input().split()
    arr = [int(i) for i in arr]
    return arr

def solve():
    n = takeintinput()[0]
    # arr = takeintinput()
    a = 1
    while(2*a<n):
        a*=2
    print(a)


for i in range(int(input())):
    solve()