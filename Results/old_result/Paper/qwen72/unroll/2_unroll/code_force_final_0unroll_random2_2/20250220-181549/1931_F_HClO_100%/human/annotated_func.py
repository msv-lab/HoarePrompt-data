#State of the program right berfore the function call: The function `func` is expected to take input through standard input or a predefined method, as the function definition does not include parameters. The input consists of multiple test cases, each starting with two integers n and k, where 1 ≤ k ≤ n ≤ 2 · 10^5 and n · k ≤ 2 · 10^5. Each of the following k lines contains n integers representing the order of participants as seen by the participant who posted the screenshot. Each integer in the screenshot is unique and within the range [1, n]. The total number of test cases, t, is such that 1 ≤ t ≤ 10^4, and the sum of n · k across all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates through each test case, reads the input for each case, and prints 'yes' or 'no' based on the conditions specified in the loop. After all iterations, the variables `t`, `n`, `m`, `a1`, `l1`, `a2`, `l2`, `l11`, `l22`, `idx1`, `idx2`, `p1`, `p2`, `val`, `a3`, and `l3` will be in their final states corresponding to the last test case processed. The variable `t` will be 0 if the loop has completed all iterations, and the other variables will hold the values from the last iteration of the loop.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input. Each test case consists of two integers `n` and `k`, followed by `k` lines of `n` unique integers each. The function processes each test case to determine if the order of participants in the screenshots can be made consistent by inserting a single participant into one of the lists. If the order can be made consistent, it prints 'yes'; otherwise, it prints 'no'. After processing all test cases, the function concludes, and the state of the program reflects the final values of the variables from the last test case processed.

