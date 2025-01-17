import heapq
def maxGCDSum(A, B, C, D):
    # Initialize variables
    n = len(A)
    pq = []
    A.sort()
    B.sort()
    C.sort()
    
    # Compute initial GCDs
    gcdA = A[0]
    gcdB = B[0]
    for i in range(n):
        gcdA = gcd(gcdA, A[i])
        gcdB = gcd(gcdB, B[i])
        
    # Push tuples into heap, tuple contains -cost and index
    for i in range(n):
        heapq.heappush(pq, (-C[i], i))
     
    # Greedily make swaps
    for _ in range(len(D)):
        d = D[_]
        while pq and d > 0:
            c, i = heapq.heappop(pq)
            if A[i] > B[i]:
                A[i], B[i] = B[i], A[i]
                gcdA = gcd(gcdA, A[i])
                gcdB = gcd(gcdB, B[i])
                d += c
        D[_] = gcdA + gcdB