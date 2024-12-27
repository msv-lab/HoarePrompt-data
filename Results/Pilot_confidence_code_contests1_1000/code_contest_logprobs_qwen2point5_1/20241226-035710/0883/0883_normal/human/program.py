if __name__ == '__main__':
    n, k = map(int, raw_input().split(' '))
    a = map(int, raw_input().split(' '))
    b = map(int, raw_input().split())

    if k == 1:
        ans = True
        for i in range(n - 1):
            if(a[i] == 0):
                a[i] = b[0]
            if a[i] >= a[i + 1]:
                ans = False
                break
        if ans:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')



