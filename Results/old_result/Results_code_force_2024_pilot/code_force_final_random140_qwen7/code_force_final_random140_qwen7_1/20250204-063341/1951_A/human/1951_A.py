t = int(input())
results = []
 
for _ in range(t):
    n = int(input())
    arr = input()
    
    count_ones = arr.count('1')
    
    if count_ones == 0:
        results.append('yes')
    elif count_ones % 2 != 0:
        results.append('no')
    elif count_ones == 2:
        if '11' in arr:
            results.append('no')
        else:
            results.append('yes')
    else:
        results.append('yes')
 
for r in results:
    print(r)