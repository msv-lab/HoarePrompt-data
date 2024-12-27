import sys
line = sys.stdin.readline().strip();
a = line.split(" ")[0];
b = line.split(" ")[1];
s = a + b;
m = 0;
for c in s :
    d = int(c);
    m = max(m, d);

t = int(a) + int(b)
ret = "";
while (t != 0):
    r = t % (m + 1);
    t //= (m + 1);
    ret = ret + str(r);
print(len(ret));