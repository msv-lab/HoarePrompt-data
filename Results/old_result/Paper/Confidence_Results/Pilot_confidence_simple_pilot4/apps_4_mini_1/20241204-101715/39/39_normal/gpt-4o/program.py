def are_tracks_same(n, L, kefa, sasha):
    def get_differences(arr):
        return [(arr[(i + 1) % n] - arr[i]) % L for i in range(n)]
    
    kefa_diff = get_differences(kefa)
    sasha_diff = get_differences(sasha)
    
    for i in range(n):
        if sasha_diff[i:] + sasha_diff[:i] == kefa_diff:
            return "YES"
    
    return "NO"

# Reading input
n, L = map(int, input().split())
kefa = list(map(int, input().split()))
sasha = list(map(int, input().split()))

# Output result
print(are_tracks_same(n, L, kefa, sasha))
