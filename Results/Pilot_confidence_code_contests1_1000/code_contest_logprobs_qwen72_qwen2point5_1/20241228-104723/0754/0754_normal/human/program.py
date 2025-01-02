def ziped(ar):
    p = []
    for i in ar:
        x = int(i.split('-')[0])
        c = i.split('-')[1]

        if len(p) > 0 and p[-1][1] == c:
            p[-1][0] += x
        else:
            p.append([x,c])


    return p

def solve(t,s,c):
    ans = 0
    if len(s) == 1:
        for i in t:
            if c(i,s[0]):
                ans += i[0] - s[0][0] + 1
        return ans
    if len(s) == 2:
        for i in range(len(t)-1):
            if c(t[i],s[0]) and c(t[i+1],s[-1]):
                ans += 1
        return  ans
    v = s[1:-1] + [[100500,'#']] + t
    p = [0]* len(v)
    for i in range(1,len(v)):
        j = p[i-1]
        while j > 0 and v[j] != v[i]:
            j = p[j-1]
        if v[j] == v[i]:
            j += 1
        p[i] = j
    for i in range(len(v)-1):
        if p[i] == len(s) - 2 and c(v[i-p[i]],s[0]) and c(v[i+1],s[-1]):
            ans += 1
    return  ans


n,m = map(int , raw_input().split())
t = ziped(raw_input().split())
s = ziped(raw_input().split())
print (solve(t,s, lambda x,y:x[1] == y[1] and x[0] >= y[0]))
