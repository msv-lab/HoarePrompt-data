T = int(input())

for case in range(1, T+1):
    N = int(input())
    people = []
    
    for _ in range(N):
        A, B, C = map(int, input().split())
        people.append((A, B, C))
    
    max_likes = 0
    
    for i in range(10001):
        for j in range(10001):
            for k in range(10001):
                count = 0
                
                for person in people:
                    if person[0] >= i and person[1] >= j and person[2] >= k:
                        count += 1
                
                max_likes = max(max_likes, count)
    
    print("Case #{}: {}".format(case, max_likes))