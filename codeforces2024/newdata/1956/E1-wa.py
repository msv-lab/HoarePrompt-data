def attack(a):
    b = a.copy()
    for i in range(len(a)-1):
        a[i+1] = max(0, a[i+1] - a[i])
    a[0] = max(0, a[0] - a[-1])
    for i in range(len(a)):
        if a[i] != b[i]:
            return 1, a
    return 0, a


def solve(a):
    update = 1
    while update:
        update, a = attack(a)
    mask = []
    index = []
    for i in range(len(a)):
        if a[i] != 0:
            mask.append(1)
            index.append(i+1)
        else:
            mask.append(0)
    return sum(mask), index


def main():
    t = int(input())
    for i in range(t):
        a = list(map(int, input().split()))
        m, index = solve(a)
        print(m)
        if m == 0:
            print("\n")
        else:
            print(*index)

if __name__ == "__main__":
    main()    