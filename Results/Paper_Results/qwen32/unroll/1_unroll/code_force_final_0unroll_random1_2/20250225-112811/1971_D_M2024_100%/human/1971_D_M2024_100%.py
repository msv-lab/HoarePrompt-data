t = int(input())
 
for _ in range(t):
    a = input()
    cut0 = 0
    cut1 = 0
    for i in range(len(a)-1):
        if a[i] == '1' and a[i+1] == '0':
            cut1 += 1
        if a[i] == '0' and a[i+1] == '1':
            cut0 += 1
    if cut0 == 0:
        print(cut1+1)
    else:
        print(cut0+cut1)
 
# 011 0 111 0 11
# 1 011