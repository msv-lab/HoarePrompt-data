t = int(input())
while t:

    import string
    n = int(input())
    # a = [0,0,0,1,0,2,0,3,1,1,4]
    a = []
    for i in range(n):
        a.append(int(input()))
    max_val = max(a)
    s = '*' * n
    letters = string.ascii_lowercase
    s = list(s)
    for i in range(max_val+1):
        k = 0
        for j in range(n):
            if a[j] == i:
                s[j] = letters[k]
                k +=1
    s = ''.join(s)
    print(s)
    t -= 1
     
