def minimal_jumps(s):
    n = len(s)
    jumps = [0] * n
    visited = [False] * n
    queue = [0]
    visited[0] = True

    while queue:
        current = queue.pop(0)
        if current == n-1:
            return jumps[current]
        
        if current > 0 and not visited[current-1]:
            queue.append(current-1)
            jumps[current-1] = jumps[current] + 1
            visited[current-1] = True
        
        if current < n-1 and not visited[current+1]:
            queue.append(current+1)
            jumps[current+1] = jumps[current] + 1
            visited[current+1] = True
        
        for i in range(n):
            if s[i] == s[current] and not visited[i]:
                queue.append(i)
                jumps[i] = jumps[current] + 1
                visited[i] = True

s = input()
print(minimal_jumps(s))