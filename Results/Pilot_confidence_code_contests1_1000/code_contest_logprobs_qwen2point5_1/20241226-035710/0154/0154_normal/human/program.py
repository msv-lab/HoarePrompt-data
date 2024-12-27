n = int(raw_input())
a = []
for i in range(n):
    a.append(int(raw_input()))

b = [ 0 if i == max(a) else i for i in a ]
if max(b) == 0:
    b = [ max(a) if i == max(a) else i for i in a ]

print([ max(b) if i == max(a) else max(a) for i in a ])