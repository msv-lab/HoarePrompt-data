n = int(input())
a = map(int, raw_input().split())

maximum_count = 0
for start in range(0, n):
    for end in range(0, n):
        if start <= end:
            #flip from a[start] to a[end]
            b = list(a) #make a copy of apply
            for i in range(start, end + 1): #flip everything
                                            #from start to end
                b[i] = 1 - b[i]
        
            #count number of ones
            count = sum(b)
            
            #update the maximum/largest so far
            maximum_count = max(maximum_count, count)

print(maximum_count)