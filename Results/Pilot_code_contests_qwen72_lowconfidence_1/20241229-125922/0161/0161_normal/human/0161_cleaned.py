cs = {1: [None] + list('abcde'), 2: [None] + list('fghij'), 3: [None] + list('klmno'), 4: [None] + list('pqrst'), 5: [None] + list('uvwxy'), 6: [None] + list('z.?! ')}
while True:
    try:
        it = iter(raw_input().strip())
    except ValueError:
        break
    try:
        r = c = None
        s = []
        while True:
            r = int(it.next())
            c = int(it.next())
            s += [cs[r][c]]
            r = c = None
    except IndexError:
        stdout.write('NA\n')
    except StopIteration:
        if not r and (not c):
            stdout.write(''.join(s) + '\n')
        else:
            stdout.write('NA\n')
        continue