t=int(raw_input())
for _ in range(t):
    s=list(raw_input())
    s.pop(-1)
    for i in range(len(s)):
        if i%2==0:
            if s[i]!='a':
                s[i]='a'
            else:
                s[i]='b'
        else:
            if s[i]!='z':
                s[i]='z'
            else:
                s[i]='y'
    print(''.join(s))
    