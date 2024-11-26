N = int(raw_input())
S = raw_input()
result = 0
for i in range(N):
    if S[i] == 'I':
        result += 1
    else:
        result -= 1
if result < 0:
    result = 0
print(result)