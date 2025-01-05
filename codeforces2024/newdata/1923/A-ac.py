
n = int(input())

answer = []

for i in range(n):
    
    num = int(input())
    
    shim = input().split(' ')
    
    
    start = 0
    end = 0
    for j in range(num):
        if shim[j] == '1':
            start = j
            break
    
    for j in range(1,num+1):
        if shim[-j] == '1':
            end = num-j
            break
    
    count = 0
    for j in range(start,end):
        if shim[j] == '0':
            count+=1
    
    answer.append(count)
    
for i in answer:
    print(i)