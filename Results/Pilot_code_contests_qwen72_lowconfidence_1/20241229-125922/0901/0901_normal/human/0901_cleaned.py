(n, m) = [int(x) for x in raw_input().split()]
start_counting = 'NO'
counter = {}
final_cnt = 0
for i in range(0, n):
    tmp_str = raw_input().split()
    state = int(tmp_str[0])
    if state == 1:
        if start_counting == 'YES':
            if len(counter):
                final_cnt += max(counter.values())
            counter = {}
        start_counting = 'YES'
    else:
        frnd = tmp_str[1]
        if frnd in counter:
            counter[frnd] += 1
        else:
            counter[frnd] = 1
if start_counting == 'YES':
    if len(counter):
        final_cnt += max(counter.values())
print(final_cnt)