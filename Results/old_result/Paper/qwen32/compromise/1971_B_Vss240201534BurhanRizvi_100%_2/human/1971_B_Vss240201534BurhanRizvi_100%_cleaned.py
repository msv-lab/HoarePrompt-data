for _ in range(int(input())):
    s = input()
    if len(s) == 1:
        print('No')
    elif len(set(s)) == 1 and len(s) > 1:
        print('No')
    else:
        s2 = ''.join(random.sample(s, len(s)))
        if s == s2:
            s2 = s[1:] + s[0]
        print('Yes')
        print(s2)