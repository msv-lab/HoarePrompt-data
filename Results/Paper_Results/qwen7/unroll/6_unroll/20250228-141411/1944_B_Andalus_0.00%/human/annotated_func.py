#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. Additionally, an array a of length 2n is given, where each integer from 1 to n appears exactly twice.
def func():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        
        lst = list(map(int, input().split()))
        
        lft = lst[:n]
        
        rgt = lst[n:]
        
        ldb = []
        
        rdb = []
        
        sng = []
        
        lft.sort()
        
        rgt.sort()
        
        for i in range(1, n):
            if lft[i] == lft[i - 1]:
                ldb.append(lft[i])
            elif i < n - 1 and lft[i] != lft[i + 1]:
                sng.append(lft[i])
        
        for i in range(1, n):
            if rgt[i] == rgt[i - 1]:
                rdb.append(rgt[i])
        
        sz = 0
        
        for elem in ldb:
            if sz >= k:
                break
            if k - sz >= 2:
                print(elem, elem, end=' ')
                sz += 2
        
        for elem in sng:
            if sz >= k:
                break
            print(elem, end=' ')
            sz += 1
        
        print()
        
        sz = 0
        
        for elem in rdb:
            if sz >= k:
                break
            if k - sz >= 2:
                print(elem, elem, end=' ')
                sz += 2
        
        for elem in sng:
            if sz >= k:
                break
            print(elem, end=' ')
            sz += 1
        
    #State: Output State: The output will consist of pairs of elements from the left part of the sorted list followed by single elements, ensuring no more than `k` elements are printed in each line. If there are repeated elements in the left part, only the first occurrence is considered for pairing. Elements in the right part are also processed similarly but after the left part. Each line will contain up to `k` elements, with repeated elements from the left part paired together if possible, and single elements from both parts appended at the end if necessary.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( T \), and for each test case, it takes two integers \( n \) and \( k \), and an array \( a \) of length \( 2n \). It sorts the array into left and right halves, identifies repeated and unique elements in the left half, and prints pairs of repeated elements and unique elements from the left half, followed by unique elements from both halves, ensuring no more than \( k \) elements are printed per line. The same process is applied to the right half of the array.

