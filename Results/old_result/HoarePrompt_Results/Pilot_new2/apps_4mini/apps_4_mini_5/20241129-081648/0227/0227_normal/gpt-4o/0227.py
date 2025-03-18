def min_variables(n, a):
    a.sort()
    assigned = set()
    assigned.add(a[0])
    m = 1

    for i in range(1, n):
        can_form = False
        for x in assigned:
            if (a[i] - x) in assigned:
                can_form = True
                break
        if not can_form:
            m += 1
        assigned.add(a[i])
    
    return m

import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(map(int, data[1:]))

print(min_variables(n, a))
