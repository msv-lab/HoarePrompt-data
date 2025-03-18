#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of two integers n and k, where 1 ≤ k ≤ n ≤ 2 · 10^5 and n · k ≤ 2 · 10^5, representing the number of chat participants and the number of participants who posted screenshots, respectively. Each of the following k lines contains n integers a_{ij}, where 1 ≤ a_{ij} ≤ n and all a_{ij} are distinct, representing the order of participants shown to the participant a_{i0}. The sum of n · k over all test cases does not exceed 2 · 10^5, and all the authors of the screenshots are different.
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
        
    #State: After all iterations of the loop, `t` is reduced to 0, and all test cases have been processed. For each test case, the loop has determined whether the conditions specified in the code are met, printing 'yes' if the conditions are satisfied for all tuples in `val` and 'no' if any tuple fails the condition. The values of `n`, `a1`, `l1`, `a2`, `l2`, `l11`, `l22`, `i`, `idx1`, `idx2`, `p1`, `p2`, and `l` are reset for each new test case, and their final values depend on the last test case processed. The list `val` is emptied after processing each test case.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers `n` and `k`, and a set of `k` lists of integers. For each test case, it determines whether the order of participants shown to each participant (as represented by the lists) can be rearranged to meet certain conditions. Specifically, it checks if the lists can be adjusted so that the order of participants is consistent across all participants. If the conditions are met, it prints 'yes'; otherwise, it prints 'no'. The function reads input from standard input and prints the results to standard output. After processing all test cases, the function concludes, and the state of the program is such that all test cases have been evaluated and the corresponding 'yes' or 'no' results have been printed.

