#State of the program right berfore the function call: t is a positive integer such that 1 \le t \le 10^4. For each test case, n and k are positive integers where 1 \le k \le n \le 2 \cdot 10^5 and n \cdot k \le 2 \cdot 10^5. Each of the k lines contains n integers a_{ij} (1 \le a_{ij} \le n) representing the order of participants shown to the participant a_{i0}, and all a_{ij} are distinct for each line. The sum of n \cdot k across all test cases does not exceed 2 \cdot 10^5, and all authors of the screenshots are different.
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
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n` and `m` from input. Depending on the values of `n` and `m`, and the lists `l1` and `l2`, it either prints 'yes' or 'no'. After all iterations, the values of `t`, `n`, and `m` are no longer relevant, and the lists `l1`, `l2`, and `l3` are modified or reset during each iteration, so they do not retain any specific state from one iteration to the next. The only consistent state is that the loop has completed `t` iterations.
#Overall this is what the function does:The function reads `t` test cases, where `t` is a positive integer (1 ≤ t ≤ 10^4). For each test case, it reads two positive integers `n` and `m` (1 ≤ k ≤ n ≤ 2 * 10^5, n * k ≤ 2 * 10^5) representing the number of participants and the number of orders, respectively. It then reads `m` lines, each containing `n` distinct integers representing the order of participants shown to a particular participant. The function checks if the orders are consistent with a specific condition and prints 'yes' if they are, or 'no' if they are not. After processing all test cases, the function has no lasting state, as all variables are reset or redefined for each test case.

