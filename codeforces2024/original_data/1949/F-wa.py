def find_good_match():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    users = []
    
    for i in range(n):
        k = int(data[index])
        activities = set(map(int, data[index+1:index+1+k]))
        users.append(activities)
        index += k + 1
    
    # Check for a good match
    for i in range(n):
        for j in range(i + 1, n):
            shared_activities = users[i] & users[j]
            unique_i = users[i] - users[j]
            unique_j = users[j] - users[i]
            
            if shared_activities and unique_i and unique_j:
                print("YES")
                print(i + 1, j + 1)
                return
    
    print("NO")