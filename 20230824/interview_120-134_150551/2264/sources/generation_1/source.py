def smallest_segment(t, tests):
    result = []
    for i in range(t):
        n = tests[i][0]
        segments = tests[i][1:]
        
        left = max([segment[0] for segment in segments])
        right = min([segment[1] for segment in segments])
        
        length = right - left + 1 if right >= left else 0
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