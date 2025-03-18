from collections import defaultdict
x, y = map(int, input().split())
lst = defaultdict(list)
rev = defaultdict(list)
for _ in range(x-1):
    a,b = map(int, input().split())
    lst[a].append(b)
    rev[b].append(a)
z = int(input())
tmp = z
one = True
while lst[tmp] != []:
    one = not one
    tmp = lst[tmp].pop()
 
two = True
tmp = z
while rev[tmp] != []:
    two = not two
    tmp = rev[tmp].pop()
 
print('Hermione'if two and one else 'Ron')