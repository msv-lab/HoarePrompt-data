def calculate_performance_increase(a, l, r, u):
    total_sections = sum(a[l-1:r])
    performance_increase = 0
    for i in range(1, total_sections + 1):
        performance_increase += max(u + 1 - i, 0)
    return performance_increase

def find_optimal_r(n, a, q, queries):
    results = []
    for l, u in queries:
        optimal_r = l
        max_performance_increase = calculate_performance_increase(a, l, l, u)
        for r in range(l + 1, n + 1):
            performance_increase = calculate_performance_increase(a, l, r, u)
            if performance_increase > max_performance_increase:
                max_performance_increase = performance_increase
                optimal_r = r
        results.append(optimal_r)
    return results

# Input reading
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    
    # Process and output results
    results = find_optimal_r(n, a, q, queries)
    for result in results:
        print(result)