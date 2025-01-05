import sys
input = sys.stdin.readline
def give_pairs(x, slots):
    mult = x // slots
    rem = x % slots
    first = slots - rem
    ans = ((2 * (x - mult) + ((first-1) * (-mult))) / 2) * first * mult
    ans += ((2 * (mult + 1) + (slots - first - 2) * (mult+1)) / 2) * (slots - first - 1) * (mult+1)

    return int(ans)

def get_val(n, arr, slots):
    ans1 = 0
    ans2 = 0
    for i in range(n):
        ans1 += give_pairs(arr[i], min(slots, arr[i]))
        ans2 += give_pairs(arr[i], min(slots + 1, arr[i]))
    return ans1, ans2


# print(give_pairs(2, 2))
def solve():
    n, b, x = map(int, input().split())
    arr = list(map(int, input().split()))

    maxi = -1
    squares = 0
    for i in range(n):
        squares += (arr[i] ** 2)
        maxi = max(maxi, arr[i])
    new_maxi = 0
    ind = 1
    for i in range(1, maxi+1):
        if b * squares * (i-1) / (2 * i) - (i-1) * x > new_maxi:
            new_maxi = b * squares * (i-1) / (2 * i) - (i-1) * x
            ind = i
    # print("TEST")
    # print(new_maxi)
    # print(ind)
    if ind == 1:
        ans1, ans2 = get_val(n, arr, 1)
        print(max(0, b * ans2 - x))
        return
    ans1, ans2 = get_val(n, arr, ind-1)
    ans2, ans3 = get_val(n, arr, ind)
    print(max(ans1 * b - (ind - 2) * x, ans2 * b - (ind - 1) * x, ans3 * b - ind * x))


for t in range(int(input())):
    solve()