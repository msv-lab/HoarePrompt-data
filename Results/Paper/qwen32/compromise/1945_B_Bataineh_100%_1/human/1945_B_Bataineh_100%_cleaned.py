t = int(input())
for i in range(t):
    (a, b, m) = map(int, input().split())
    if m < a and m < b:
        print(2)
    elif m < a and m > b:
        print(2 + m // b)
    elif m < b and m > a:
        print(2 + m // a)
    else:
        print(m // a + m // b + 2)