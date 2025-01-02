def napoleon_cake_1(arr, layers):
    res = [0 for i in range(layers)]
    for a in range(0, len(arr)):
        if arr[a] == 0:
            continue
        res[a] += 1
        idx = a-arr[a]
        if idx > 0:
            res[idx] -= 1
        
    for i in range(len(res)-2, -1, -1):
        res[i] += res[i+1]
    lst = [str(1) if i >= 1 else str(0) for i in res]

    return ' '.join(lst)

n = int(raw_input())
for i in range(0, n):
	layers = int(raw_input())
	lst = raw_input().split(" ")
	lst = [int(i) for i in lst]
	print(napoleon_cake_1(lst, layers))