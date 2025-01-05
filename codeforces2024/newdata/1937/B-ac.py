import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr1 = input().strip()
    arr2 = input().strip()

    up_pos = -1
    lst_p = -1

    for i in range(n-1):
        if arr1[i+1] != arr2[i]:
            if arr1[i+1] > arr2[i] and up_pos == -1:
                up_pos = i
                break
            lst_p = i

    if up_pos == -1:
        if lst_p == -1:
            print(arr1 + arr2[-1])
            print(n)
        else:
            print(arr1 + arr2[-1])
            print(n - lst_p - 1)
    else:
        print(arr1[:up_pos+1] + arr2[up_pos:])
        print(up_pos-lst_p)