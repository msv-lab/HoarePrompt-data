def min_new_problems(t, test_cases):
    results = []
    for case in test_cases:
        n, a, b = case
        count = 0 
        for i in range(n):
            while a[i] > b[i]:
                
                a.append(b[i])
                a.sort()  
                a.pop() 
                count += 1
        results.append(count)
    return results


t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, a, b))


results = min_new_problems(t, test_cases)
print("\n".join(map(str, results)))
