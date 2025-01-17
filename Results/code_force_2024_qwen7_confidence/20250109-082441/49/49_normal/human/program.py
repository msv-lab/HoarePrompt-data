t = int(input())
#n = int(input())
#P = input().rstrip().split(' ')
#S = list(input().rstrip())    

def ProcessAns(A, query, d, ans):
    start = len(A) - 1
    end = 0

    for q in query:
        start = min(q[0], start)
        end = max(q[1], end)

    summation = [0]
    progression = [0]

    s = start

    k = 1

    indexHash = {}

    while s <= end:
        summation.append(summation[-1] + A[s])
        progression.append(progression[-1] + k * A[s])
        indexHash[s] = len(summation) - 1
        k += 1
        s += d

    for q in query:
        s = indexHash[q[0]]
        e = indexHash[q[1]]
        index = q[2]

        #print(e, len(A), len(progression))
        
        ans[index] = progression[e] - progression[s-1]
        ans[index] -= (s - 1) * (summation[e] - summation[s-1])

def Query(A, query, d, ans):

    s = query[0][0]
    e = query[0][1]

    process = [query[0]]

    for i in range(1, len(query)):
        if e <= query[i][0]:
            e = max(e, query[i][1])
            process.append(query[i])
        else:
            ProcessAns(A, process, d, ans)
            process = []

    ProcessAns(A, process, d, ans)

def SolveE():
    P = input().rstrip().split(' ')
    A = input().rstrip().split(' ')
    n, q = int(P[0]), int(P[1])

    for i in range(len(A)):
        A[i] = int(A[i])

    queries = {}

    for i in range(q):
        P = input().rstrip().split(' ')
        s, d, k = int(P[0])-1, int(P[1]), int(P[2])
        l = s
        if (d, s%d) in queries:
            queries[(d, s%d)].append((s, s + d*(k-1), i))
        else:
            queries[(d, s%d)] = [(s, s + d*(k-1), i)]

        #queries.append((, , ))

    ans = [0] * q

    for key in queries:
        queries[key].sort()
        Query(A, queries[key], key[0], ans)

    arr = []

    for i in range(len(ans)):
        arr.append(str(ans[i]))
        arr.append(" ")

    arr.pop()
    
    return "".join(arr)
        
    


for i in range(t):
    print(SolveE())