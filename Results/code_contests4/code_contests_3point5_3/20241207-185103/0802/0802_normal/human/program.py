f = open("input.txt", "r")
input = map(lambda x : int(x), f.read().strip().split("\n"))
f.close()
d, n, m = input[0], input[1], input[2]
S, K = set(sorted([0]+input[3:3+n-1])), input[3+n-1:]
sum = 0
for k in K:
	i = 1
	while (True):
		if (k+i)%8 in S or (k-i)%8 in S: break
		i += 1
	sum += i
f = open("output.txt", "w")
f.write(str(sum))
f.close()