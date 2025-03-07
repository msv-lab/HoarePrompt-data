def func_1():
    t = int(input())
    for _ in range(t):
        (n, k) = map(int, input().split())
        a = list(map(int, input().split()))
        x = list(map(int, input().split()))
        monsters = sorted(zip(x, a), key=lambda p: abs(p[0]))
        bullets_used = 0
        can_survive = True
        for (pos, health) in monsters:
            distance = abs(pos)
            total_bullets_needed = bullets_used + health
            if total_bullets_needed > distance * k:
                can_survive = False
                break
            bullets_used += health
        print('YES' if can_survive else 'NO')
if __name__ == '__main__':
    func_1()