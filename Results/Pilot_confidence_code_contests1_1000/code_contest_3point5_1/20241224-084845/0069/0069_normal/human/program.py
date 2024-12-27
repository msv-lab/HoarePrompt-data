count = 0
total = 0
while 1:
	try:
		s = raw_input()
	except:
		break
	if len(s) == 0:
		break
	if s[0] == '+':
		count += 1
	elif s[0] == '-':
		count -= 1
	else:
		index = s.index(':')
		length = len(s)-index-1
		total += length * count
	

