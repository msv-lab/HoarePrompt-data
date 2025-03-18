#State of the program right berfore the function call: t is a positive integer, and for each test case, n and k are positive integers such that 1 ≤ k ≤ n ≤ 2 ⋅ 10^5 and n ⋅ k ≤ 2 ⋅ 10^5. Each screenshot is represented as a list of n distinct integers ranging from 1 to n. All authors of the screenshots are unique across all test cases.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        if m == 1:
            input()
            print('yes')
            continue
        
        a1, *l1 = map(int, input().split())
        
        a2, *l2 = map(int, input().split())
        
        l11 = [i for i in l1 if i != a2]
        
        l22 = [i for i in l2 if i != a1]
        
        if l11 != l22:
            for _ in range(m - 2):
                input()
            print('no')
            continue
        
        idx1 = idx2 = -1
        
        p1 = p2 = 0
        
        for i in range(n - 1):
            if i + max(p1, p2) == n - 1:
                break
            if l1[i + p1] != l2[i + p2]:
                if l1[i + p1] == a2 and l2[i + p2] == a1:
                    idx1 = idx2 = i
                    break
                else:
                    if l1[i + p1] == a2:
                        idx1 = i
                        p1 = 1
                    else:
                        idx2 = i
                        p2 = 1
                    if idx1 >= 0 and idx2 >= 0:
                        break
        
        val = []
        
        if idx1 < idx2:
            l2.insert(idx1, a2)
            l = l2
        elif idx1 > idx2:
            l1.insert(idx2, a1)
            l = l1
        else:
            if m == 2:
                print('yes')
                continue
            a3, *l3 = map(int, input().split())
            if l3.index(a1) < l3.index(a2):
                l1.insert(idx2, a1)
                l = l1
            else:
                l2.insert(idx1, a2)
                l = l2
            val.append((a3, l3))
            m -= 1
        
        for _ in range(m - 2):
            a3, *l3 = map(int, input().split())
            val.append((a3, l3))
        
        for a3, l3 in val:
            if l3 != [i for i in l if i != a3]:
                print('no')
                break
        else:
            print('yes')
        
    #State: The output state depends on the inputs provided during each iteration of the loop. The final output will be 'yes' if all conditions are met throughout the iterations, otherwise 'no'. Each 'yes' or 'no' output is determined based on the logic inside the loop, which checks for matching sequences and specific conditions involving the integers provided.
#Overall this is what the function does:The function processes multiple test cases, each consisting of positive integers \(t\), \(n\), and \(m\), along with two lists of \(n\) distinct integers. It checks if certain conditions are met across these lists and inserts specific values to ensure the lists match. If all conditions are satisfied, it prints 'yes'; otherwise, it prints 'no'. The function does not return any value but outputs 'yes' or 'no' based on the logic executed within the test cases.

