def string(s):
    s3 = list(s)
    i = 1
    j = 0
    s1 = ''
    while i < len(s3):
        if s[i] != s[i - 1]:
            s3.pop(i)
            s3.pop(i - 1)
            s = s1.join(s3)
            j += 1
            i = 0
        else:
            i += 1
            continue

        i += 1
    if j == 0 or j % 2 == 0:
        w="NET"
    else:
        w="DA"
    return w
s5=[]
for t in range(int(raw_input())):
    s = raw_input()
    a=str(s)
    s5.append(a)
for t1 in s5:
    print(t1)