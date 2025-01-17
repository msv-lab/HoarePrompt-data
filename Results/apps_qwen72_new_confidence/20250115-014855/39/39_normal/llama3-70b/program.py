n, L = map(int, input().split())
kefa = list(map(int, input().split()))
sasha = list(map(int, input().split()))

def normalize(arr, L):
    arr = [(x - min(arr)) % L for x in arr]
    arr.sort()
    return arr

kefa_norm = normalize(kefa, L)
sasha_norm = normalize(sasha, L)

print("YES" if kefa_norm == sasha_norm else "NO")
