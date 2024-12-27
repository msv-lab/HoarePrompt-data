l = raw_input().split()
s = l[0]

def get_removals(s):
    ret = []
    for i in range(len(s) - 1):
        if int(s[i]) + int(s[i + 1]) == 1:
            ret.append(i)
    return ret

def remove(s, index):
    if index == 0:
        return s[2:]
    if index == (len(s) - 1):
        return s[:index-1]
    return  s[0:index] + s[index + 2:]

num_removals = []

ones = 0
zeros = 0
for num in s:
    if num == '0':
        ones += 1
    if num == '1':
        zeros += 1
max_candidate = min(ones, zeros) * 2

def process(s, count):
    removals = get_removals(s)
    if len(removals) == 0:
        num_removals.append(count)
        if count == max_candidate:
            print(max_candidate)
            exit()
        return
    count += 2
    max_remove = 0
    ss = []
    for removal in removals:
        s1 = remove(s, removal)
        ss.append(s1)
        num_removes = len(get_removals(s1))
        if max_remove < num_removes:
            max_remove = num_removes
    for s1 in set(ss):
        if len(get_removals(s1)) == max_remove:
            process(s1, count)

# process(s, 0)
print(max_candidate)
