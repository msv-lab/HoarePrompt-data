#State of the program right berfore the function call: The function `func` is not properly defined for the problem. The correct function definition should include parameters for the number of test cases, the number of participants, the number of screenshots, and the screenshots themselves. For example, it should be defined as `def func(t, n, k, screenshots):` where `t` is an integer representing the number of test cases, `n` and `k` are integers such that 1 ≤ k ≤ n ≤ 2 · 10^5 and n · k ≤ 2 · 10^5, and `screenshots` is a list of lists, each containing `n` integers representing the order of participants shown to the participant who posted the screenshot.
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
        
    #State: The output state after the loop executes all the iterations is that the variable `t` will be reduced to 0, and the loop will have printed either 'yes' or 'no' for each iteration based on the conditions specified in the loop. The variables `n`, `m`, `l1`, `l2`, `l3`, `a1`, `a2`, `a3`, `idx1`, `idx2`, `p1`, `p2`, and `val` will have been modified and used within the loop, but their final values will depend on the input provided during each iteration.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the number of participants and the number of screenshots, then reads the order of participants shown in each screenshot. The function determines if the order of participants can be consistently derived from the screenshots. If the order is consistent, it prints 'yes'; otherwise, it prints 'no'. The function does not return any value. After processing all test cases, the function concludes, and the output will be a series of 'yes' or 'no' for each test case.

