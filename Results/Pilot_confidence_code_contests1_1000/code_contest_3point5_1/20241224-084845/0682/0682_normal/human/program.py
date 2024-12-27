s = raw_input().strip()
keys = [ None for i in range(int(raw_input())) ]
for i in range(len(keys)):
    keys[i] = raw_input().strip()
best_length, best_pos = 0, 0

def kosher(left, right):
    pos_range = range(right - 1, left - 1, -1)
    #print(left, right)
    for key in keys:
        for pos in pos_range:
            key_pos = len(key) - right + pos
            #print(pos, key, key_pos)
            if key_pos == -1 or key[key_pos] != s[pos]:
                break
            if key_pos == 0:
                return False
    return True

left, right = 0, 0
while True:
        if kosher(left, right + 1):
            right += 1
            length = right - left
            if length > best_length:
                best_length = length
                best_pos = left
            if right == len(s):
                break
        else:
            left += 1

print('%d %d' % (best_length, best_pos))
