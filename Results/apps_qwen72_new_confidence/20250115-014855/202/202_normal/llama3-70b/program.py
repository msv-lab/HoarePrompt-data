C, Hr, Hb, Wr, Wb = map(int, input().split())

max_joy = 0
for r in range(C // Wr + 1):
    b = (C - r * Wr) // Wb
    joy = r * Hr + b * Hb
    max_joy = max(max_joy, joy)

print(max_joy)
