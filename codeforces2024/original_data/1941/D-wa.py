

t = int(input())
for _ in range(t):
    n, m, x = map(int, input().split())
    queue = []
    for __ in range(m):
        d, c = input().split()
        d = int(d)
        if len(queue) == 0:
            queue.append(x)

        length = len(queue)
        
        for ___ in range(length):
            if c == '0':
                queue.append((queue[0]+d) % n if (queue[0]+d) != n else n)
            elif c == '1':
                queue.append(n - (d-queue[0]) if queue[0] < d else queue[0]-d)
            elif c == '?':
                queue.append((queue[0]+d) % n if (queue[0]+d) != n else n)
                queue.append(n - (d-queue[0]) if queue[0] <= d else queue[0]-d)
            queue.pop(0)
            length -= 1
        queue = list(set(queue))
    queue.sort()
    print(len(queue))
    for i in queue:
        print(i, end=" ")
    print()
 
        