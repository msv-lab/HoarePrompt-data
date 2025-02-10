t = int(input().strip())
 
for i in range(t):
    # n is no. books
    n = int(input().strip())
    ls = input().split()
    last = int(ls.pop())
    other = int(sorted(ls).pop())
    print(last + other)