n, m = map(int, raw_input().split())

set_list = []

for i in range(m):
        set_list.append(set())

for i in range(n):
        s = raw_input()
        for j in range(m):
                set_list[j].add(s[j])
