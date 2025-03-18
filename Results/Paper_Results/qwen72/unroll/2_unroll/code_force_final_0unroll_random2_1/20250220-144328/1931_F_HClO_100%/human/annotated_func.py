#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case contains two integers n and k where 1 ≤ k ≤ n ≤ 2 · 10^5 and n · k ≤ 2 · 10^5, representing the number of chat participants and the number of participants who posted screenshots, respectively. Each of the following k lines contains n integers a_{ij} where 1 ≤ a_{ij} ≤ n and all a_{ij} are distinct, representing the order of participants shown to the participant a_{i0}. The sum of n · k for all test cases does not exceed 2 · 10^5, and all the authors of the screenshots are different.
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
        
    #State: The loop iterates `t` times, processing each test case. For each test case, the loop reads `n` and `k`, and then reads `k` lines of integers. The loop checks if the order of participants shown to each participant is consistent with the conditions specified. If the conditions are met, it prints 'yes' for that test case; otherwise, it prints 'no'. After all test cases are processed, the initial state of `t` is unchanged, and the variables `n`, `k`, `a1`, `a2`, `l1`, `l2`, `l11`, `l22`, `idx1`, `idx2`, `p1`, `p2`, and `val` are reset for each new test case.
#Overall this is what the function does:The function processes a series of test cases, each defined by the number of chat participants (`n`) and the number of participants who posted screenshots (`k`). For each test case, the function reads `k` lines of `n` distinct integers, representing the order of participants shown to the participant who posted the screenshot. The function checks if the order of participants shown to each participant is consistent with the conditions specified. If the conditions are met for all participants in a test case, it prints 'yes'; otherwise, it prints 'no'. After processing all test cases, the function has no side effects on the input variables, and the state of the program is reset for each new test case.

