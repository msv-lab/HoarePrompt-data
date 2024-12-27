n = int(raw_input())
z, o = 0, 1023
for _ in xrange(n):
	op, num = raw_input().split()
	num = int(num)
	z, o = eval("{0} {1} {2}".format(z, op, num)), eval("{0} {1} {2}".format(o, op, num))

n2, n3, n4 = 0, 0, 1023
for i in xrange(10):
	x = (1 << i)
	q = z & x
	w = o & x
	if q and (not w) == 0:
		n2 |= x
	elif q and w:
		n3 |= x
	elif (not q) and (not w):
		n4 &= ~x

print(3)
print("^ " + str(n2))
print("| " + str(n3))
print("& " + str(n4))
