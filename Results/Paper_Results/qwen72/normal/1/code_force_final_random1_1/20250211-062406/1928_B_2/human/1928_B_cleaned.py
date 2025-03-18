def func_1():
    return int(input())

def func_2():
    return map(int, input().split())

def func_3():
    return list(map(int, input().split()))

def func_4():
    return sorted(list(map(int, input().split())))

def func_5():
    return map(str, input().split())

def func_6():
    return list(input())

def func_7():
    return sorted(list(map(str, input().split())))

def func_8(arr):
    ans = []
    tem = 1
    for i in range(len(arr)):
        tem *= arr[i]
        ans.append(tem)
    return ans

def func_9(arr):
    ans = []
    tem = 1
    for i in range(len(arr) - 1, -1, -1):
        tem *= arr[i]
        ans.append(tem)
    return ans
for _ in range(func_1()):
    n = func_1()
    arr = sorted(list(set(func_3())))
    m = max(arr)
    ans = 0
    for i in range(len(arr)):
        a = bisect_left(arr, arr[i] + n)
        d = a - i
        ans = max(ans, d)
    print(ans)