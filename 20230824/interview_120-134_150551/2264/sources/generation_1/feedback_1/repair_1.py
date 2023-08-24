def smallest_segment(t, tests):
    result = []
    for test in tests:
        n = test[0]
        segments = test[1:]
        
        left = min([segment[0] for segment in segments])
        right = max([segment[1] for segment in segments])
        
        length = right - left if right >= left else 0
        result.append(length)
    
    return result

t = int(input())
tests = []
for _ in range(t):
    n = int(input())
    segments = []
    for _ in range(n):
        segment = tuple(map(int, input().split()))
        segments.append(segment)
    tests.append([n] + segments)

result = smallest_segment(t, tests)
for res in result:
    print(res)