#State of the program right berfore the function call: t is a positive integer, and for each test case, n and k are positive integers such that 1 ≤ k ≤ n ≤ 2 ⋅ 10^5 and n ⋅ k ≤ 2 ⋅ 10^5. Each screenshot description is a list of n distinct integers between 1 and n, inclusive.
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
        
    #State: Output State: `a3` is the first element of the fifth tuple in `val`, `l3` is the second element of the fifth tuple in `val`, `val` is a list containing five tuples, each being a pair consisting of `a3` and `l3`, and `m` is equal to 3.
    #
    #This means that after the loop has executed all its iterations, the value of `a3` will be the first element of the fifth tuple added to the `val` list, and `l3` will be the second element of that same tuple. The `val` list will contain exactly five such tuples. Additionally, the variable `m` will be reduced to 3 after processing all inputs according to the logic within the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers \(n\) and \(m\), and lists of integers. For each test case, it checks if two modified lists can be made identical through specific operations. If possible, it prints 'yes' and constructs a list of additional tuples; otherwise, it prints 'no'. The function ultimately outputs 'yes' only if all constructed tuples maintain the required condition, or 'no' if any fail.

