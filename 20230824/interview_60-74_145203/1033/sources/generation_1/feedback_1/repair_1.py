import math

def minimum_spots(n, H):
    if n <= H:
        return 1
    else:
        return H + math.ceil((n - H) / 2)

n, H = map(int, input().split())
print(minimum_spots(n, H))