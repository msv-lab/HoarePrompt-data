n,k = map(int,raw_input().split())
all = map(int,raw_input().split())

minn = min(all)
fail = False
amount = 0
for i in all:
    if (i-minn) % k != 0:
        fail = True
    else:
        amount += (i-minn)/k
if fail:
    print(-1)
else:
    print(amount)