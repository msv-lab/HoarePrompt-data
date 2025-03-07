#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. Each test case consists of two integers n and k (1 ≤ k ≤ n ≤ 2 · 10^5, n · k ≤ 2 · 10^5), where n is the number of chat participants and k is the number of participants who posted screenshots. Each of the k lines contains n integers a_{ij} (1 ≤ a_{ij} ≤ n, all a_{ij} are distinct), representing the order of participants shown to the participant a_{i0}, who is the author of the screenshot. All authors of the screenshots are different.
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
        
    #State: The loop has completed all iterations without breaking, meaning for every tuple `(a3, l3)` in `val`, `l3` was equal to `[i for i in l if i != a3]`. The final state is that `t` is 0, indicating all test cases have been processed. For each test case, `m` is greater than 2, `val` contains `m-2` tuples, each tuple being `(a3, l3)` from each iteration, and the program prints 'yes' for each test case. All other variables (`_`, `a3`, `l3`, `val`, `n`, `a1`, `l1`, `a2`, `l2`, `l11`, `l22`, `p1`, `p2`, `idx1`, `idx2`) retain their final values from the last iteration of the loop for each test case.
#Overall this is what the function does:The function processes a series of test cases, each defined by the number of chat participants `n` and the number of participants who posted screenshots `k`. For each test case, it reads the order of participants shown to each screenshot author and determines whether the order of participants can be consistently aligned across all screenshots. If the orders are consistent, the function prints 'yes'; otherwise, it prints 'no'. After processing all test cases, the function completes, and the final state is that all test cases have been evaluated and the appropriate 'yes' or 'no' responses have been printed for each.

