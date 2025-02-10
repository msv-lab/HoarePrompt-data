a = int(input())
s = 0
 
for i in range(a):
    d = int(input()) 
    b = input()
    for j in range(len(b)):
        if b[j] == '@':
            s = s+1
        elif b[j] == '*':
            if j==len(b) - 1:
                break
            elif b[j+1] == '*':
                break
            
    print(s)
    s = 0