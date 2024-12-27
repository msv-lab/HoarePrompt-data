num = int(raw_input())
a = raw_input().split()
a = [int(x) for x in a]
a.sort()
a.reverse()
sereja = 0
dima = 0

for i in range(0,len(a),2):
    sereja = sereja + a[i]

for i in range (1,len(a),2):
    dima = dima + a[i]

print("{} {}".format(sereja,dima))
