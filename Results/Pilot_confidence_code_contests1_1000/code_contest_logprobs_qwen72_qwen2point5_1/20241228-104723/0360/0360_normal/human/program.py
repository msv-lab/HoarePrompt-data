try: input = raw_input
except: pass

def slow():
    for i in range(n-m+1):
        for k in range(m):
            result[i+k] = (result[i+k] + key[k]) % c

def faster():
    total = sum(key)
    inckeys = []
    t = 0
    for i in range(m):
        t += key[i]
        inckeys.append(t)
    lastkeys = []
    t = 0
    for i in range(m-1, 0, -1):
        t += key[i]
        lastkeys.append(t)
    lastkeys.reverse()
    for i in range(0, min(m, n-m+1)):
        result[i] = (result[i] + inckeys[i]) % c
    for i in range(min(m, n-m+1), n-m+1):
        result[i] = (result[i] + total) % c
    for i in range(n-m+1, n):
        result[i] = (result[i] + lastkeys[i % (n-m+1)]) % c
    return result
        

n, m, c = list(map(int, input().split()))
msg = list(map(int, input().split()))
key = list(map(int, input().split()))
result = [start for start in msg]
faster()
print(" ".join(map(str, result)))