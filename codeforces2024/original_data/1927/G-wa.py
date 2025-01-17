def min_charges_to_paint(t, test_cases):
    results = []
    for test in test_cases:
        n, a = test
        painted = [False] * n  
        charge_count = 0       
        
        i = 0  
        while i < n:
            if not painted[i]:  
                charge_count += 1
                left_start = max(0, i - a[i] + 1)
                right_end = min(n - 1, i + a[i] - 1)
                
                for j in range(left_start, right_end + 1):
                    painted[j] = True
            
            i += 1
        
        results.append(charge_count)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = min_charges_to_paint(t, test_cases)

for res in results:
    print(res)
