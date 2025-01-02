(n, big) = map(int, raw_input().split())
total = [str(big)]
temp = big
while big > n:
    if big % 2 == 0:
        big = big / 2
        total.append(str(big))
    else:
        temp = (big - 1) // 10
        if temp * 10 + 1 == big:
            total.append(str(temp))
            big = temp
        else:
            break
if total[-1] == str(n):
    sys.stdout.write('YES\n%d\n' % len(total) + ' '.join(total[::-1]) + '\n')
else:
    sys.stdout.write('NO\n')