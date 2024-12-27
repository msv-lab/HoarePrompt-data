# vim: set fileencoding=utf-8 :
k, s = map(int, raw_input().split())
patterns = []
ct = 0

for x in range(k + 1):
    nokori = s - x
    for y in range(k + 1):
        if 0 <= nokori - y <= k:
            ct += 1

print(ct)
