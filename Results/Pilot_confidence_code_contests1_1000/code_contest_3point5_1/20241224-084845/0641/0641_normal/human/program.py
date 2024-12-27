#To take input
# str = raw_input()
# R = float(str.split()[0])
# real = int(str.split()[1])
# R, x1, y1, x2, y2 = map(int, raw_input().split(' '))
# print "{} {} {}".format(x3, y3, r)

n, a, b = map(int, raw_input().split(' '))
i=0
if((a>n/2 and b<=n/2) or (a<=n/2 and b>n/2)):
    print("Final!")
    exit(0)

while(a!=b):
    i += 1
    a = (a+1)/2
    b = (b+1)/2

print(i)
