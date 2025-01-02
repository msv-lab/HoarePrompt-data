n = input()
s = raw_input()
d = {}
for i in range(1, n):
    gram = s[i - 1:i + 1]
    if d.get(gram) == None:
        d[gram] = 1
    else:
        d[gram] += 1
a = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(a[0][0])