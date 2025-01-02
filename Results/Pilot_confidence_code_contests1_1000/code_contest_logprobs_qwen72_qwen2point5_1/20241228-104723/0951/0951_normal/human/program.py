input = raw_input
range = xrange

from collections import Counter

def answer():
    m = int(input())
    half_m = m / 2.

    ps = map(int, input().split(" "))
    c = Counter(ps)

    keys = sorted(c.keys())

    gold_key = keys[-1]
    gold_num = c[gold_key]

    other_keys = keys[0:-1]

    if len(other_keys) == 0:
        return "0 0 0"

    cur_num = 0
    ok = False
    for key_i, key in enumerate(other_keys):
        val = c[key]
        cur_num += val
        if cur_num >= half_m:
            ok = True
            break

    if not ok:
        return "0 0 0"

    no_num = cur_num

    other_keys = other_keys[key_i+1:]
    bronze_num = 0
    ok = False
    for key_i, key in enumerate(other_keys):
        val = c[key]
        bronze_num += val
        if bronze_num > gold_num:
            ok = True
            break
    if not ok:
        return "0 0 0"

    other_keys = other_keys[key_i+1:]

    silver_num = m - bronze_num - no_num - gold_num
    if gold_num > silver_num:
        return "0 0 0"
   
    out = "%d %d %d" % (gold_num, silver_num, bronze_num)
    return out

n = int(input())
for i in range(n):
    out = answer()
    print(out)