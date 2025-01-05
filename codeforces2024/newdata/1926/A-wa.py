n  = int(input())
num_A = int(0)
num_B = int(0)
for i in range (0, n):
    x = input()
    for j in x:
        if j == 'A':
           num_A +=1 
        else:
            num_B +=1
    if num_A > num_B:
           print("A")
    else:
           print("B")