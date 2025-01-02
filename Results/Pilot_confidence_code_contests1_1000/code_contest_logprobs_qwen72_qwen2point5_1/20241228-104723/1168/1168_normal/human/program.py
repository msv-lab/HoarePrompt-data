try: input = raw_input
except: pass

def slow():
    result = [r for r in msg]
    for i in range(n-m+1):
        for k in range(m):
            result[i+k] = (result[i+k] + key[k]) % c
    return result

def faster():
    result = [r for r in msg]
    total = sum(key)
    inckeys = []
    t = 0
    for i in range(m):
        t += key[i]
        inckeys.append(t)
    lastkeys = []
    for i in range(m-1):
        lastkeys.append(total - inckeys[i])
    
        
    for i in range(0, min(m, n-m+1)):
        result[i] = (result[i] + inckeys[i]) % c
    for i in range(m, n-m+1):
        result[i] = (result[i] + total) % c
    k = 0
    for i in range(n-m+1, n):
        t = lastkeys[k] if i >= m - 1 else lastkeys[k] - lastkeys[len(lastkeys) - 1 - (m - i - 2)]
        result[i] = (result[i] + t) % c
        k += 1
    return result
        

n, m, c = list(map(int, input().split()))
msg = list(map(int, input().split()))
key = list(map(int, input().split()))
#r1 = slow()
r2 = faster()
#if r1 != r2:
#    print("No match!")
#    print(" ".join(map(str, enumerate(r1))))
print(" ".join(map(str, r2)))