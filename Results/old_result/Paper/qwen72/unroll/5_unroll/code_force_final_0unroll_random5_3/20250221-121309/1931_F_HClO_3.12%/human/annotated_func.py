#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case contains two integers n and k such that 1 ≤ k ≤ n ≤ 2 · 10^5 and n · k ≤ 2 · 10^5, representing the number of chat participants and the number of participants who posted screenshots, respectively. Each of the following k lines contains n integers a_{ij} (1 ≤ a_{ij} ≤ n, all a_{ij} are different) representing the order of participants as seen by the participant a_{i0}, who is the author of the screenshot and always appears at the top of their own list. The sum of n · k for all test cases does not exceed 2 · 10^5, and all authors of the screenshots are different.
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
        
    #State: For each test case, the loop will output either 'yes' or 'no' based on the conditions described in the loop. The variables `t`, `n`, `m`, `a1`, `a2`, `l1`, `l2`, `l11`, `l22`, `idx1`, `idx2`, `p1`, `p2`, and `val` will be reset or updated for each iteration of the loop, but their final values after the loop completes are not relevant to the output state. The output state will be a series of 'yes' or 'no' for each test case, indicating whether the conditions for the chat participants' order are met.
#Overall this is what the function does:The function processes multiple test cases, each involving a chat scenario with `n` participants and `k` participants who posted screenshots. For each test case, it reads the order of participants as seen by each screenshot author and determines whether the order of participants can be consistently rearranged to match across all screenshots. The function outputs 'yes' if the orders can be consistently rearranged, and 'no' otherwise. After processing all test cases, the function's final state is a series of 'yes' or 'no' outputs corresponding to each test case.

