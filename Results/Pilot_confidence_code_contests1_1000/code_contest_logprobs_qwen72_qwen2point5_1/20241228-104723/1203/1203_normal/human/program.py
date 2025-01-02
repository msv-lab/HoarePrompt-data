def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    res = 0
    count = 0
    for i in range(n):
        c = int(format(a[i],'b'))
        res += c
    res = str(res)
    for i in range(len(res)):
        if int(res[i]) % 2 == 0:
            print('Furlo')
            return
    print('Rublo')

main()