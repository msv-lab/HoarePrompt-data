import sys

HEIGHT = 20000

# with open('input.txt', 'r') as f:

f = sys.stdin
height = HEIGHT
n = int(f.readline())
sat = True
for i in range(n):
	dst, directon = f.readline().strip().split(' ')
	if directon not in {'South', 'North'}:
		continue
	if directon == 'South':
		height -= int(dst)
	elif directon == 'North':
		height += int(dst)
	else:
		raise ValueError('Invalid directon')
	if height < 0 or height > HEIGHT:
		sat = False
		break
sat &= height == HEIGHT
print('YES' if sat else 'NO')
