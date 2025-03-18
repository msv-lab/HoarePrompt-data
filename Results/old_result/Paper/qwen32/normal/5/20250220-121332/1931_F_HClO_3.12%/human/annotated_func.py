#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each of the t test cases, n and k are integers such that 1 ≤ k ≤ n ≤ 2 · 10^5 and n · k ≤ 2 · 10^5. Each of the k lines following the description of each test case contains n distinct integers a_{ij} each (1 ≤ a_{ij} ≤ n), where a_{i0} is the author of the screenshot and is always at the top of the list. All authors of the screenshots are different.
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
        
    #State: t is 0, n and m remain unchanged, a1 and a2 remain the same, l2 and l22 are updated based on the last iteration's conditions, idx1 and idx2 are updated based on the last iteration's conditions, p1 and p2 remain the same, val contains m - 2 tuples (a3, l3) from the input, l is updated based on the last iteration's conditions. The loop has printed 'yes' or 'no' for all test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of screenshots and their respective authors. For each test case, it determines if it's possible to reorder the screenshots such that the specified authors are at the top of their respective lists and the order of other authors is consistent across all lists. The function outputs "yes" if such a reordering is possible, otherwise "no".

