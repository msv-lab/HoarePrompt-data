x_p, y_p, x_v, y_v = map(int, input().split())

if x_p <= x_v and y_p <= y_v:
    print("Polycarp")
else:
    print("Vasiliy")
