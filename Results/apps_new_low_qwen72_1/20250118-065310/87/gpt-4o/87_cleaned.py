(x_p, y_p, x_v, y_v) = map(int, input().split())
polycarp_distance = max(x_p, y_p)
vasiliy_distance = max(x_v, y_v)
if polycarp_distance <= vasiliy_distance:
    print('Polycarp')
else:
    print('Vasiliy')