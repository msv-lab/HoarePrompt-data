for _ in range(int(input())):
    n = int(input())
 
    #Find first item
    k = 1
    for i in range(2, n):
        print('?', 0, k, 0, i, flush=True)
        res = input()
        if res == '<':
            k = i
 
    #Find second item    
    best = 0
    for i in range(1, n):
        print('?', k, best, k, i, flush=True)
        res = input()
        if res == '<':
            best = i
 
    print('!', k, best, flush = True)