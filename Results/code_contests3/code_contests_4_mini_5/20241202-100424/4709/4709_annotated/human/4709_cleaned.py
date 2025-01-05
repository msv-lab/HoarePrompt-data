a = raw_input()
l = a.split()
A = l[0]
B = l[1]
ans = 0
if int(A) == int(B):
    ans = 1
for i in range(int(A), int(B)):
    C = list(str(i))
    if C[0] == C[4] and C[1] == C[3]:
        ans += 1
print(ans)