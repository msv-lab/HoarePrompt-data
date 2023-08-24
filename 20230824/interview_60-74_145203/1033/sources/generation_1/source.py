import math

def minimum_spots(n, H):
    if n <= H:
        return math.ceil(n/2)
    else:
        return H + math.ceil((n - H) / 2)

n, H = map(int, input().split())
print(minimum_spots(n, H))