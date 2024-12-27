y = int(input())
yes = []
for _ in range(y) :
    x = yes.append(int(input()))
i = 1
if (yes[0] - yes[i] == 0) or (yes[0] + yes[i] == 2*yes[i+1]) or (yes[0] + yes[1] == yes[2]):
    if (yes[0] + yes[i] + yes[i+1] == 360) :
        print('YES')
    else :
        print('NO')

