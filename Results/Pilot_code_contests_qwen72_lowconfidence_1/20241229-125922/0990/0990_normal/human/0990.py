n = int(raw_input()) 
a = [int(x) for x in raw_input().split()] 


"""
max_avg = 0
max_len = 0
for i in range(0, n):
    for j in range(i, n):
        tmp = sum(a[i:j+1])/float(j-i+1)
        if tmp > max_avg:
            max_avg = tmp
            max_len = (j-i+1)
        elif tmp == max_avg:
            if (j-i+1) > max_len:
                max_len = (j-i+1)
"""

max_a = max(a)
#print (max_a)
max_len = 0
tmp = 0
for i in range(0,n):
    if a[i]!=max_a:
        if tmp > max_len:
            max_len = tmp
        tmp = 0
    elif a[i]==max_a:
        tmp += 1
if tmp > max_len:
    max_len = tmp


print (max_len)



