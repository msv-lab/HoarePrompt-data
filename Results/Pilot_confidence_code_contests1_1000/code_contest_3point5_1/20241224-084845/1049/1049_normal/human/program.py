# coding: utf-8
lis = []
n = input()
current = -1
su = 0
final = 0
last = -1
u = raw_input().split(" ")
lis = []
for i in u:
	lis.append(int(i))
lis.sort()
for i in lis[::-1]:
	if (current == -1):
		current = i
		last = i
		su = 1
	else:
		j = i
		if (j == current):
			su += 1
		else:
			if (j >= last-su):
				su += 1
			else:
				if (su > last):
					final += (last+1)*last/2
				else:
					final += (2*last-su+1)*su/2
				su = 1
				last = j
			current = j
if (su > last):
	final += (last+1)*last/2
else:
	final += (2*last-su+1)*su/2
print(final)
	