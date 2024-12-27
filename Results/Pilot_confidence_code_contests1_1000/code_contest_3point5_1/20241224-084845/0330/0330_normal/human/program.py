s = raw_input()

x = str()
tmp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(26):
	if s.count(tmp[i]) == 2:
		x = tmp[i]
		break

a = s.split(x)

if a[1] == '':
	print('Impossible')
elif a[0] == '' and a[2] == '':
	print(x + a[1][:12])
	print(a[1][:-14:-1])
elif a[0] == '':
	x1 = a[2][:12 - (len(a[1]) // 2)]
	x2 = a[1][:(len(a[1]) // 2)]
	x3 = a[2][12 - (len(a[1]) // 2):]
	x4 = a[1][(len(a[1]) // 2):]
	print(x1[::-1] + x + x2)
	print(x3 + x4[::-1])
elif a[2] == '':
	a = s[::-1].split(x)
	x1 = a[2][:12 - (len(a[1]) // 2)]
	x2 = a[1][:(len(a[1]) // 2)]
	x3 = a[2][12 - (len(a[1]) // 2):]
	x4 = a[1][(len(a[1]) // 2):]
	print(x1[::-1] + x + x2)
	print(x3 + x4[::-1])
else:
	a = ['', a[1], a[2] + a[0]]
	x1 = a[2][:12 - (len(a[1]) // 2)]
	x2 = a[1][:(len(a[1]) // 2)]
	x3 = a[2][12 - (len(a[1]) // 2):]
	x4 = a[1][(len(a[1]) // 2):]
	print(x1[::-1] + x + x2)
	print(x3 + x4[::-1])
