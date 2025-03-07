#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where 1 <= a_i <= 100 for all i in range n.
def func():
    t = int(input())
    for i in range(t):
        a = input()
        
        b = list(map(int, a.split()))
        
        o = input().split()
        
        n = b[0]
        
        f = b[1]
        
        k = b[2]
        
        if k == n:
            print('YES')
            continue
        
        fav = o[f - 1]
        
        dic = {i: o.count(i) for i in o}
        
        o.sort(reverse=True)
        
        if o.index(fav) > k - 1:
            print('NO')
            continue
        
        l = sorted(list(set(o)), reverse=True)
        
        for i in range(len(l)):
            if fav != l[i]:
                k -= dic[l[i]]
                if k <= 0:
                    print('NO')
                    break
            else:
                k -= dic[l[i]]
                if k < 0:
                    print('MAYBE')
                    break
                else:
                    print('YES')
                    break
        
    #State: The output state depends on the input values provided during each iteration of the loop. The final output will be 'YES', 'NO', or 'MAYBE' based on the conditions checked within the loop for each iteration. If any condition leads to a 'NO' or 'MAYBE' being printed, that will be the final output for that specific test case. If all conditions lead to a 'YES', then 'YES' will be the final output.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a list of integers `a`, two indices `f` and `k`, and a sequence of strings `o`. It checks if a specific element in `o` (identified by index `f`) can be moved up to position `k` in the sorted order of unique elements in `o`. Based on the result of this check, it prints either 'YES', 'NO', or 'MAYBE'. The final output for each test case is determined by the conditions evaluated within the function.

