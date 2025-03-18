#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 2 · 10^5 and n · k ≤ 2 · 10^5, representing the number of chat participants and the number of participants who posted screenshots, respectively. Each of the k lines contains n integers a_{ij} (1 ≤ a_{ij} ≤ n, all a_{ij} are different), representing the order of participants shown to the participant a_{i0}, where a_{i0} is the author of the screenshot and always appears at the top of the list. The sum of n · k for all test cases does not exceed 2 · 10^5, and all authors of the screenshots are different.
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
        
    #State: `t` is 0, `n` and `m` are integers such that 1 ≤ k ≤ n ≤ 2 · 10^5 and n · k ≤ 2 · 10^5 for each test case, `a1`, `a2`, and `a3` are integers representing the authors of the screenshots, `l1`, `l2`, and `l3` are lists of integers representing the order of participants shown to the authors of the screenshots, `l11` and `l22` are lists containing elements from `l1` and `l2` respectively, excluding `a2` and `a1`, `i` is `n - 2`, `idx1` and `idx2` are either both -1 or both set to the index where `l1[i + p1] == a2` and `l2[i + p2] == a1`, or one of them is set to the index where `l1[i + p1] == a2` and the other is set to the index where `l2[i + p2] == a1`, `p1` and `p2` are either both 0 or one of them is 1, `val` contains tuples of the form `(a3, l3)`, and the loop has printed 'yes' or 'no' for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by the number of chat participants `n` and the number of participants who posted screenshots `k`. For each test case, it reads the order of participants shown to each screenshot author. The function then determines if the order of participants can be made consistent across all screenshots by inserting the author of one screenshot into the list of another screenshot at the correct position. If the order can be made consistent, it prints 'yes' for that test case; otherwise, it prints 'no'. After processing all test cases, the function concludes, and the state of the program is that all test cases have been evaluated and the results have been printed.

