def can_form_complete_binary_tree(n, a):
   
    freq = [0] * (n + 1)  
    
    for dist in a:
        freq[dist] += 1
    
    max_depth = max(a)
    
    for i in range(max_depth + 1):
        if freq[i] > 2:
            return "YES"
    
    return "NO"

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    
    result = can_form_complete_binary_tree(n, a)
    print(result)
