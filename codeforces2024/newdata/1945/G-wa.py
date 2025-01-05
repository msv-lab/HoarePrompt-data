import heapq

t = int(input())
for _i in range(t):
    n, d = map(int, input().split())
    students = []
    for i in range(n):
        k, s = map(int, input().split())

        # standart heapq returns min in pop, so we multiply k by -1 tp get max
        students.append((k * -1, s))

    # list of lists of who to add at specific time (end of minute)
    to_add = [[] for _ in range(d + 2)]

    p = 0
    suffix_max = [0] * n
    suffix_max[n - 1] = students[n - 1][0]
    for i in range(n - 2, -1, -1):
        # we multiplied by -1 so we find min()
        suffix_max[i] = min(students[i][0], suffix_max[i + 1])

    heap = []
    heapq.heapify(heap)
    ans = -1

    for current_sec in range(1, d + 2):
        max_prior_heap = 0
        if len(heap):
            max_prior_heap = heap[0][0]

        if suffix_max[p] > max_prior_heap:
            # take from heap
            student = heapq.heappop(heap)
        else:
            # take from original queue
            student = students[p]
            p += 1
            
        if current_sec + student[1] <= d + 1:
            to_add[current_sec + student[1]].append(student)

        if p == n:
            ans = current_sec
            break

        for student in to_add[current_sec]:
            heapq.heappush(heap, student)

    print(ans)