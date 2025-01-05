cur = []
for i in range(int(input())):
    s = raw_input()
    if s == 'pwd':
        print('/' + '/'.join(cur))
    else:
        s = s.split()[1]
        if s[0] == '/':
            cur = []
            s = s[1:]
        for x in s.split('/'):
            if x == '..':
                cur = cur[:-1]
            else:
                cur.append(x)