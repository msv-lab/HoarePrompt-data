def gb114():
    for t in range(int(input())):
        s = input()
        h = s[:2]
        if h == '00':
            print('12', end='')
        elif int(h) <= 12:
            print(h, end='')
        else:
            print('0{}'.format(int(h) - 12), end='')
        print(s[2:], ['AM', 'PM'][int(h) >= 12])
gb114()