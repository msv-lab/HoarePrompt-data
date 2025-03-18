#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100, and a is a list of n integers where 1 <= a_i <= 100 for all i.
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
        
    #State: Output State: The loop has executed all its iterations, and the final state of the variables is as follows:
    #
    #- `i` is equal to the length of list `l`.
    #- `a` is the last input string received.
    #- `b` is a list of integers obtained by splitting `a` and converting each part to an integer.
    #- `o` is a list of strings sorted in reverse order.
    #- `n` is the first element of list `b`.
    #- `f` is the second element of list `b`.
    #- `k` is the third element of list `b` minus the sum of `dic[l[-1]]` and `dic[l[-2]]` (if `l` has at least two elements), otherwise just the third element of list `b`.
    #- `fav` is the element at index `f - 1` of list `o` if `k` is equal to `n`, otherwise no new variables are introduced.
    #- `dic` is a dictionary where keys are elements of list `o` and values are their counts in list `o`.
    #- `l` is a list of unique elements from `o` sorted in reverse order.
    #
    #After all iterations, the loop has completed its execution. Depending on the conditions within the loop, one of the following outputs has been printed: 'NO', 'MAYBE', or 'YES'. If no output was printed, it means the loop did not meet any of the conditions to print 'NO' or 'MAYBE', and thus the final state of `k` reflects the cumulative subtraction of dictionary values corresponding to the elements of `l` from the third element of list `b`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a list of integers `a` of length `n`, and two additional integers `f` and `k`. It then checks if it's possible to remove up to `k` elements from the list such that the `f`-th element remains in the list. Based on the conditions met, it prints either 'YES', 'NO', or 'MAYBE'. If none of the conditions are met, it prints nothing. After processing all test cases, the function does not return anything but prints the results directly.

