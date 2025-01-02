H,W,N = map(int, raw_input().split())
sr,sc = map(int, raw_input().split())
S = raw_input()
T = raw_input()
AO = [1,W,1,H]
flag = 0
for i in reversed(range(N)):
	if(i != N-1):
		if(T[i] == 'L'):
			AO[1] = min(W,AO[1]+1)
		elif(T[i] == 'R'):
			AO[0] = max(1,AO[0]-1)
		elif(T[i] == 'U'):
			AO[3] = min(H,AO[3]+1)
		elif(T[i] == 'D'):
			AO[2] = max(1,AO[2]-1)
	if(S[i] == 'L'):
		AO[0] += 1
	elif(S[i] == 'R'):
		AO[1] -= 1
	elif(S[i] == 'U'):
		AO[2] += 1
	elif(S[i] == 'D'):
		AO[3] -= 1
	if(AO[0] > AO[1] or AO[2] > AO[3]):
		flag = 1
		break
if(AO[0] > sc or AO[1] < sc or AO[2] > sr or AO[3] < sr):
	flag = 1
if(flag == 0):
	print("YES")
else:
	print("NO")