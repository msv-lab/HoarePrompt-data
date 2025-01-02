(a, b) = map(int, raw_input().split())
(c, d) = map(int, raw_input().split())
if b == d:
    print(b)
    sys.exit()
t = d - b
for x in range((a * c + d + b) / a + 11):
    if (a * x - t) % c == 0:
        print(b + a * x)
        sys.exit()
print(-1)