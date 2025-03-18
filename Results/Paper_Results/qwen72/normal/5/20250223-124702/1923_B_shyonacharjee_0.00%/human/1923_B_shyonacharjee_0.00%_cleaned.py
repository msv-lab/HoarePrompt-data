def func_1():
    t = int(input())
    for _ in range(t):
        (n, k) = map(int, input().split())
        healths = list(map(int, input().split()))
        positions = list(map(int, input().split()))
        monsters = sorted(zip(positions, healths), key=lambda x: abs(x[0]))
        total_bullets_used = 0
        success = True
        for i in range(n):
            (position, health) = monsters[i]
            distance = abs(position)
            time_available = distance
            bullets_needed = health
            if total_bullets_used + bullets_needed > time_available:
                success = False
                break
            total_bullets_used += bullets_needed
        print('YES' if success else 'NO')
if __name__ == '__main__':
    func_1()