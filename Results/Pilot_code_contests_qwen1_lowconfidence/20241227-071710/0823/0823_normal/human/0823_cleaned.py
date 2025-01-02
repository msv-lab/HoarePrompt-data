a = [int(x) for x in stdin.readline().split()]
if abs(a[2] - a[3]) > 1:
    print(-1)
else:
    (tem, tem2) = (['4'], ['7'])
    (four, seven) = (1, 0)
    (four2, seven2) = (0, 1)
    for i in range(a[2] + a[3]):
        if i & 1:
            tem.append('4')
            tem2.append('7')
            four += 1
            seven2 += 1
        else:
            tem.append('7')
            tem2.append('4')
            four2 += 1
            seven += 1
    if (four > a[0] or seven > a[1]) and (four2 > a[0] or seven2 > a[1]):
        print(-1)
    else:
        if (four > a[0] or seven > a[1]) or a[2] < a[3]:
            (tem, four, seven) = (tem2, four2, seven2)
        (ext4, ext7) = ('4' * (a[0] - four), '7' * (a[1] - seven))
        if tem[-1] == '7':
            print('%s%s%s%s' % (tem[0], ext4, ''.join(tem[1:]), ext7))
        else:
            print('%s%s%s%s%s' % (tem[0], ext4, ''.join(tem[1:-1]), ext7, tem[-1]))