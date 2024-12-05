(k1, k2, k3) = map(int, input().split())
gcd_k1_k2 = math.gcd(k1, k2)
gcd_all = math.gcd(gcd_k1_k2, k3)
if gcd_all == 1:
    print('YES')
else:
    print('NO')