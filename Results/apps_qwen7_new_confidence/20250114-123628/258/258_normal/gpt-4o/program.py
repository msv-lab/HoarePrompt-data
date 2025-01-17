import math
import sys
input = sys.stdin.read

def is_feasible(meats, K, T):
    N = len(meats)
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1, c1 = meats[i]
            x2, y2, c2 = meats[j]
            if c1 * T < c2 * T:
                x1, y1, c1, x2, y2, c2 = x2, y2, c2, x1, y1, c1
            d = c1 * T - c2 * T
            if d < 0:
                continue
            d /= c1 * c2
            cx = (x1 + x2) / 2
            cy = (y1 + y2) / 2
            dx = (x1 - x2) / 2
            dy = (y1 - y2) / 2
            d2 = dx * dx + dy * dy
            if d * d2 > d2:
                continue
            mx = cx + dy * math.sqrt(d2 * d - d * d) / d2
            my = cy - dx * math.sqrt(d2 * d - d * d) / d2
            count = sum(c * math.sqrt((mx - x) ** 2 + (my - y) ** 2) <= T for x, y, c in meats)
            if count >= K:
                return True
    return False

def min_time_to_grill(N, K, meats):
    low, high = 0, 1e9
    while high - low > 1e-7:
        mid = (low + high) / 2
        if is_feasible(meats, K, mid):
            high = mid
        else:
            low = mid
    return high

def main():
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    meats = []
    index = 2
    for _ in range(N):
        x = int(data[index])
        y = int(data[index + 1])
        c = int(data[index + 2])
        meats.append((x, y, c))
        index += 3
    result = min_time_to_grill(N, K, meats)
    print(f"{result:.6f}")

if __name__ == "__main__":
    main()
