def func_1(x, y):
    for i in range(1, 32):
        if x >> i - 1 & 1 == y >> i - 1 & 1:
            return False
    return True

def func_2(n, integers):
    groups = []
    for num in integers:
        placed = False
        for group in groups:
            if func_1(num, group[0]):
                group.append(num)
                placed = True
                break
        if not placed:
            groups.append([num])
    return len(groups)

def func_3():
    t = int(input())
    for _ in range(t):
        n = int(input())
        integers = list(map(int, input().split()))
        print(func_2(n, integers))
if __name__ == '__main__':
    func_3()