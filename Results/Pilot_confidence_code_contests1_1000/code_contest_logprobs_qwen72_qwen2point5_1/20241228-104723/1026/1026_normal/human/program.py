sd = raw_input()
t = raw_input()
lnsd = len(sd)
lnt = len(t)
sa = 0
tru = None
for i in range(lnsd - lnt + 1):
    for i2 in range(lnt -1):
        a = sd[(0+sa):(lnt+sa)]
        if a[i2] != t[i2] and a[i2] != "?":
            break
        if i2 == lnsd -lnt:
            tru= i
    sa = sa+1
if tru == None:
    print("UNRESTORABLE")
    exit()
sd = list(sd)
for i in range(lnt):
    sd[tru+i]=t[i]
strn ="".join(sd)
print(strn.replace("?", "a"))
