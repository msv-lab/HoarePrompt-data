n = int(input())
votes = input().strip()
d_queue = []
r_queue = []
for (i, v) in enumerate(votes):
    if v == 'D':
        d_queue.append(i)
    else:
        r_queue.append(i)
while d_queue and r_queue:
    d_index = d_queue.pop(0)
    r_index = r_queue.pop(0)
    if d_index < r_index:
        d_queue.append(d_index + n)
    else:
        r_queue.append(r_index + n)
if d_queue:
    print('D')
else:
    print('R')