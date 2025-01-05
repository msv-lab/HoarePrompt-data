from typing import List

def solve(arr: List[int], n: int):
    if n == 1:
        return 1
    
    arr.sort()
    arr2 = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            continue
        else:
            arr2.append(arr[i])
    i = 0
    j = 0
    res = 1
    counter = 0
    while j < len(arr2):
        if arr2[j] - arr2[i] < n:
            counter += 1
            res = max(res, counter)
        else:
            i += 1
        j += 1
    res = max(res, counter)
    print(res)    


def test_case():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    solve(arr, n)

t = int(input())
for i in range(t):
    test_case()