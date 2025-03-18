def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        total_water = sum(a)
        target = total_water // n
        current_balance = 0
        possible = True
        for i in range(n):
            current_balance += a[i] - target
            if current_balance < 0:
                possible = False
                break
        if possible:
            print('YES')
        else:
            print('NO')
if __name__ == '__main__':
    func_1()