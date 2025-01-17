for _ in range(int(input())):
    n = int(input())
    if bin(n).count('1') & 1:
        print('second')
    else:
        print('first')
        l = int(bin(n)[3:], 2)
        print(n ^ l, l)
    while True:
        (a, b) = map(int, input().split())
        if a == b:
            break
        n = b if bin(a).count('1') & 1 else a
        l = int(bin(n)[3:], 2)
        print(n ^ l, l)