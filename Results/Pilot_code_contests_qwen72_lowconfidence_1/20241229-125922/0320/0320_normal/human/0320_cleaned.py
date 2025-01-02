n = int(raw_input())
a = map(int, raw_input().split())
zero = [i for i in a if i == 0]
pos = [i for i in a if i > 0]
neg = [i for i in a if i < 0]
if len(pos) == 0:
    pos.append(neg.pop())
    pos.append(neg.pop())
if len(neg) % 2 == 0:
    zero.append(neg.pop())
s = str(len(neg))
for i in neg:
    s += ' ' + str(i)
print(s)
s = str(len(zero))
for i in zero:
    s += ' ' + str(i)
print(s)
s = str(len(pos))
for i in pos:
    s += ' ' + str(i)
print(s)