n = int(raw_input())
arr = [int(__) for __ in raw_input().split()]
arr.sort(reverse=True)
newl = list()
fl = 0
for el in arr:
    if fl == 0:
        newl.append(el)
        fl = 1
    else:
        newl = [el] + newl
        fl = 0
print(' '.join([str(x) for x in newl]))