(na, ma) = [int(buf) for buf in stdin.readline().strip().split()]
a = [int(stdin.readline().strip()[::-1], 2) for i in range(0, na)]
(nb, mb) = [int(buf) for buf in stdin.readline().strip().split()]
b = [int(stdin.readline().strip()[::-1], 2) for i in range(0, nb)]

def func_1(x):
    x = (x & 113427455640312821154458202477256070485) + (x >> 1 & 113427455640312821154458202477256070485)
    x = (x & 68056473384187692692674921486353642291) + (x >> 2 & 68056473384187692692674921486353642291)
    x = (x & 20016609818878733144904388672456953615) + (x >> 4 & 20016609818878733144904388672456953615)
    x = (x & 1324055902416102970674609367438786815) + (x >> 8 & 1324055902416102970674609367438786815)
    x = (x & 5192217631581220737344928932233215) + (x >> 15 & 5192217631581220737344928932233215)
    x = (x & 79228162495817593524129366015) + (x >> 16 & 79228162495817593524129366015)
    x = (x & 18446744073709551615) + (x >> 32 & 18446744073709551615)
    return x

def func_2(x, y):
    cnt = 0
    for i in range(0, na):
        if i + x in range(0, nb):
            if y > 0:
                cnt += func_1(a[i] << y & b[i + x])
            else:
                cnt += func_1(a[i] & b[i + x] << -y)
    return cnt
(ans, xx, yy) = (0, 0, 0)
for x in range(1 - na, nb):
    for y in range(1 - ma, mb):
        val = func_2(x, y)
        if ans < val:
            (ans, xx, yy) = (val, x, y)
print('%d %d' % (xx, yy))