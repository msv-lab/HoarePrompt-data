#State of the program right berfore the function call: t is a positive integer, and for each test case, n and k are positive integers such that 1 ≤ k ≤ n ≤ 2⋅10^5 and n⋅k ≤ 2⋅10^5. Each test case consists of k lines, where the i-th line contains n integers representing the order of participants seen by the i-th user who posted a screenshot. All integers in each line are unique and within the range [1, n]. The sum of n⋅k across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The loop has completed all its iterations without breaking, and the final output printed is 'yes'. All the conditions inside the loop have been satisfied throughout its execution, ensuring that no contradictions arise between the lists `l1` and `l2` after all insertions and checks. The variable `val` contains a list of tuples `(a3, l3)` for each iteration beyond the initial two, and `idx1` and `idx2` are integers indicating the positions where insertions were made, if any. The values of `p1` and `p2` are either 0 or 1, depending on the path taken through the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves k lines of n unique integers ranging from 1 to n. It determines the order of participants seen by each of the k users and checks if the orders can be made consistent by inserting specific elements in certain positions. If the orders can be made consistent without contradictions, it prints 'yes'; otherwise, it prints 'no'. The function does not return any explicit value but prints the result for each test case.

