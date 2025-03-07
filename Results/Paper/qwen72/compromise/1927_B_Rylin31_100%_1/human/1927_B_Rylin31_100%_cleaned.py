for i in range(int(input())):
    l = int(input())
    s = [0 for i in range(l)]
    array = list(map(int, input().split()))
    ans = ''
    for j in array:
        ans += chr(s[j] + 97)
        s[j] += 1
    print(ans)