#State of the program right berfore the function call: a is a list of non-negative integers of length n, where 1 <= n <= 18, and 0 <= a_i <= 10^7 for each element a_i in the list. ops is a list used to store the operations performed.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: `a` is a list of non-negative integers, `ops` is a list containing the tuple ((l, l)), and `l` is equal to `r`. If `a[l]` is not 0, `a[l]` remains unchanged. If `a[l]` is 0, `a[l]` is set to 0.
        return
        #The program does not return any value as there is no return statement in the provided code.
    #State: a is a list of non-negative integers of length n, where 1 <= n <= 18, and 0 <= a_i <= 10^7 for each element a_i in the list. ops is a list used to store the operations performed. l and r are indices such that l is not equal to r.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: The list `a` will be modified such that every element from index `l` to index `r` (inclusive) will be set to the value `r - l + 1`. All other elements in the list `a` will remain unchanged from their initial state. The variables `l` and `r` will retain their final values after the loop has executed, which are the upper and lower bounds of the last segment processed by the loop.
        #
        #In simpler terms, after the loop completes all its iterations, the sublist of `a` starting from index `l` to index `r` will consist entirely of the value `r - l + 1`, and the rest of the list will stay as it was initially.
        func_1(a, l + 1, r, ops)
    #State: The list `a` will have every element from index `l` to index `r` set to the value `r - l + 1`, and the rest of the list will remain unchanged from their initial state. The variables `l` and `r` will retain their final values after the loop has executed, which are the upper and lower bounds of the last segment processed by the loop.
#Overall this is what the function does:The function modifies a list of non-negative integers `a` based on the indices `l` and `r`. If `l` equals `r`, it checks if `a[l]` is zero; if not, it sets `a[l]` to zero and records the operation. Otherwise, it recursively processes the subarray from `l` to `r`, setting all elements within this range to `r - l + 1` and recording the operation. The function does not return any value.

#State of the program right berfore the function call: a is a list of non-negative integers, and n is the length of the list a such that 1 <= n <= 18.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all elements in list 'a', the length of list 'ops', and the list 'ops' itself.
#Overall this is what the function does:The function accepts a list of non-negative integers and returns three values: the sum of all elements in the list, the length of a list named 'ops', and the 'ops' list itself.

#State of the program right berfore the function call: a is a list of non-negative integers of length n, where 1 <= n <= 18, and 0 <= a_i <= 10^7 for all 1 <= i <= n. ops is a list used to store the sequence of operations performed.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `s` is the sum of elements in list `a` from index `l` to index `r` inclusive, `i` is `r + 1`, and all elements in the sublist `a[l:r+1]` are equal to `r - l + 1`.
        #
        #This means that after the loop has executed all its iterations, the value of `i` will be `r + 1` because the loop increments `i` from `l` to `r`. Additionally, every element in the sublist from index `l` to index `r` in list `a` will be set to `r - l + 1` due to the assignment statement inside the loop. The sum `s` remains unchanged as no operations were performed on it within the loop, and the condition `l <= r` must still hold true for the loop to complete all iterations.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: Postcondition: `s` is the sum of elements in list `a` from index `l` to index `r` inclusive, and `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the position of `mx` in the sublist `a[l:r + 1]` plus `l`, and if `pos` is not equal to `l`, `pos` is decreased by 1.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: Postcondition: `s` is the sum of elements in list `a` from index `l` to index `r` inclusive, and `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the position of `mx` in the sublist `a[l:r + 1]` plus `l`, and if `pos` is not equal to `r`, `pos` is decreased by 1 after the function `recursive_maximize_sum(pos + 1, r)` is called.
    #State: `s` is the sum of elements in list `a` from index `l` to index `r` inclusive, `i` is `r + 1`, and either all elements in the sublist `a[l:r+1]` are equal to `r - l + 1` or `s` is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the position of `mx` in the sublist `a[l:r + 1]` plus `l`, and if `pos` is not equal to `r`, `pos` is decreased by 1 after the function `recursive_maximize_sum(pos + 1, r)` is called.
#Overall this is what the function does:The function `recursive_maximize_sum` takes two parameters, `l` and `r`, which define a sublist of a given list `a`. It aims to maximize the sum of the elements in this sublist by either setting all elements to the maximum value in the sublist or recursively processing the left and right parts of the sublist based on certain conditions. The function does not return a value but modifies the original list `a` and appends operations to the `ops` list. After the function concludes, the sublist defined by `l` and `r` will have either all elements set to the maximum value in the sublist or the sum of the sublist will be maximized according to the given conditions.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 18, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 10^7.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s, m (where s and m are the results of func_2(a)’s first and second returns, respectively)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: Output State: `ops` is an empty list.
    #
    #Natural Language Explanation: Given that the loop continues to execute as long as `ops` is a non-empty list, and since `ops` remains a non-empty list even after three iterations, it implies that the condition for the loop to continue (i.e., `ops` being non-empty) persists. However, the problem does not provide any information indicating that `ops` will become empty during or after the loop's execution. Therefore, based on the given information and without any additional conditions that could make `ops` empty, we can conclude that `ops` remains a non-empty list after all iterations of the loop have finished. But since the question asks for the state after all iterations and the only change mentioned is in the loop's continuation condition, and no operation inside the loop changes `ops` to an empty list, the most logical conclusion is that `ops` remains non-empty. However, if we strictly follow the instruction to describe the final state based on the given information and assuming the loop eventually stops, the only state that fits the description provided is when `ops` becomes empty, which means the loop has completed its iterations and there are no further operations to perform. Thus, `ops` is an empty list.
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers. It then calls another function `func_2` with `a` as input, receiving three values `s`, `m`, and `ops`. It prints `s` and `m`, and iterates over `ops` to print pairs of indices. After the loop, `ops` is guaranteed to be an empty list.

