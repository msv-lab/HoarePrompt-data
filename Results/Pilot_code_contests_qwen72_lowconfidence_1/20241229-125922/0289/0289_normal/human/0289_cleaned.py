R = raw_input()
Q = R.split()
g = int(Q[1])
W = raw_input()
V = W.split()
l = len(V)
B = []
for i in range(l):
    B.append(int(V[i]))
A = sorted(B)
count = l
k = 0
for i in range(l):
    while A[k] - A[i] <= g:
        k += 1
        if k == l:
            break
    if l - k + i < count:
        count = l - k + i
        rm_elem_lower = A[:i]
        rm_elem_upper = A[k:]
        rm_elem_total = rm_elem_lower + rm_elem_upper
    if k == l:
        break
print(count)