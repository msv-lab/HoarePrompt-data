#State of the program right berfore the function call: t is a positive integer, and for each test case, n and k are positive integers such that 1 ≤ k ≤ n ≤ 2 ⋅ 10^5 and n ⋅ k ≤ 2 ⋅ 10^5. Each screenshot description is a list of n distinct integers ranging from 1 to n, representing the order of participants as seen by the respective user.
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
        
        if idx1 == -1 and idx2 != -1:
            idx1 = n - 2
        
        if idx2 == -1 and idx1 != -1:
            idx2 = n - 2
        
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
        
    #State: Output State: The loop has executed all its iterations, and the final output is 'yes'. This means that for all the inputs provided, the conditions within the loop were satisfied such that no contradiction was found when checking the lists `l3` against the modified list `l` for each `a3`. Specifically, for every tuple `(a3, l3)` in `val`, the list `l3` did not match the list comprehension `[i for i in l if i != a3]`. Therefore, the loop concluded by printing 'yes', indicating consistency across all provided inputs.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two lists of integers. For each test case, it checks if certain conditions are met and modifies the lists accordingly. If all conditions are satisfied without any contradictions, it prints 'yes'; otherwise, it prints 'no'. The function ensures that for each element `a3` and its corresponding list `l3` in a validation list `val`, the list `l3` matches the modified list `l` after removing `a3`.

