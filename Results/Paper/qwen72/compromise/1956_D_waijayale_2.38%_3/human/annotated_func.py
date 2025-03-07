#State of the program right berfore the function call: a is a list of integers, l and r are integers such that 0 <= l <= r < len(a), and ops is a list that will store tuples of integers representing the operations performed.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: *`a` is a list of integers, `l` and `r` are integers such that 0 <= l <= r < len(a), and `l` == `r`. If `a[l]` is not 0, then `ops` is a list that contains one tuple `(l, l)`. Otherwise, `ops` remains unchanged.
        return
        #The program returns None.
    #State: *a is a list of integers, l and r are integers such that 0 <= l <= r < len(a), and ops is a list that will store tuples of integers representing the operations performed. Additionally, l is not equal to r.
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: `a` is a list of integers where all elements from index `l` to index `r` (inclusive) have been set to `r - l + 1`. The list `ops` contains the tuple `(l, r)`. The values of `l` and `r` remain unchanged.
        func_1(a, l + 1, r, ops)
    #State: *`a` is a list of integers, and `l` and `r` are integers such that 0 <= l <= r < len(a). If `a[l]` is not equal to `r - l + 1`, then all elements from index `l + 1` to index `r` (inclusive) in `a` have been set to `r - (l + 1) + 1`, and the list `ops` contains the tuples `(l, r)` and `(l + 1, r)`. The values of `l` and `r` remain unchanged.
#Overall this is what the function does:The function `func_1` accepts a list of integers `a`, two integers `l` and `r` such that 0 <= l <= r < len(a), and a list `ops` to store tuples of integers representing operations. It modifies the list `a` and appends tuples to `ops` based on certain conditions. If `l` equals `r` and `a[l]` is not 0, it sets `a[l]` to 0 and appends `(l, l)` to `ops`. If `l` is not equal to `r` and `a[l]` is not equal to `r - l + 1`, it sets all elements from index `l` to `r` in `a` to `r - l + 1` and appends `(l, r)` to `ops`. The function does not return any value, returning `None` instead. After the function concludes, the list `a` may have some of its elements modified, and the list `ops` may contain tuples representing the operations performed. The values of `l` and `r` remain unchanged.

#State of the program right berfore the function call: a is a list of integers such that 1 <= len(a) <= 18 and 0 <= a[i] <= 10^7 for all 0 <= i < len(a).
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all integers in list `a`, the length of list `ops` which is 0, and the list `ops` which is empty.
#Overall this is what the function does:The function `func_2` accepts a list `a` of integers and returns the sum of all integers in `a`, the length of an empty list `ops` (which is 0), and the empty list `ops` itself. The function does not modify the input list `a` or perform any operations that affect the state of the program outside of its scope.

#State of the program right berfore the function call: l and r are integers such that 0 <= l <= r < n, where n is the length of the array a. a is a list of integers where each element a_i satisfies 0 <= a_i <= 10^7. ops is a list that will store the operations as tuples (l, r).
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: The elements in the sublist `a[l:r + 1]` are all set to the value `r - l + 1`. The variables `l`, `r`, `n`, `ops`, and `s` remain unchanged.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: *`l` and `r` are integers such that 0 <= `l` <= `r` < `n`, `a` is a list of integers where each element `a_i` satisfies 0 <= `a_i` <= 10^7, `ops` is a list that will store the operations as tuples (`l`, `r`), `s` is the sum of the elements in the sublist `a[l:r + 1]` and is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the index of `mx` in the original list `a`. If `pos` is not equal to `l`, the function `recursive_maximize_sum` is called with arguments `l` and `pos - 1`.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: *`l` and `r` are integers such that 0 <= `l` <= `r` < `n`, `a` is a list of integers where each element `a_i` satisfies 0 <= `a_i` <= 10^7, `ops` is a list that will store the operations as tuples (`l`, `r`), `s` is the sum of the elements in the sublist `a[l:r + 1]` and is greater than `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the index of `mx` in the original list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum` is called with `l` = `pos + 1` and `r` = `r`. If `pos` is equal to `r`, no further recursive call is made.
    #State: *`l` and `r` are integers such that 0 <= `l` <= `r` < `n`, `a` is a list of integers where each element `a_i` satisfies 0 <= `a_i` <= 10^7, `ops` is a list that will store the operations as tuples (`l`, `r`), and `s` is the sum of the elements in the sublist `a[l:r + 1]`. If `s` <= `(r - l + 1) * (r - l + 1)`, the elements in the sublist `a[l:r + 1]` are all set to the value `r - l + 1`, and `l`, `r`, `n`, `ops`, and `s` remain unchanged. If `s` > `(r - l + 1) * (r - l + 1)`, `mx` is the maximum value in the sublist `a[l:r + 1]`, `pos` is the index of `mx` in the original list `a`. If `pos` is not equal to `r`, the function `recursive_maximize_sum` is called with `l` = `pos + 1` and `r` = `r`. If `pos` is equal to `r`, no further recursive call is made.
#Overall this is what the function does:The function `recursive_maximize_sum` accepts two integers `l` and `r` and a list of integers `a`. It modifies the sublist `a[l:r+1]` by setting all elements to the value `r - l + 1` if the sum of the elements in this sublist is less than or equal to the square of the sublist's length. Otherwise, it recursively processes the left and right sublists around the maximum element in the sublist. The function also appends tuples `(l, r)` to the list `ops` when the sublist is modified. The final state of the program is that the list `a` may have been modified, and `ops` contains tuples representing the ranges of sublists that were modified. The function itself does not return a value.

#State of the program right berfore the function call: No variables are passed to the function `func_3()`. The function reads `n` and `a` from standard input, where `n` is an integer such that 1 ≤ n ≤ 18, and `a` is a list of `n` integers where each integer `a_i` satisfies 0 ≤ a_i ≤ 10^7.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s, m (where s is the sum of all elements in the list a and m is the maximum element in the list a)
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: `n` is an integer such that 1 ≤ n ≤ 18, `a` is a list of integers input by the user where each integer `a_i` satisfies 0 ≤ a_i ≤ 10^7, `s`, `m`, and `ops` are the values returned by `func_2(a)`.
#Overall this is what the function does:The function `func_3` reads an integer `n` (1 ≤ n ≤ 18) and a list `a` of `n` integers (0 ≤ a_i ≤ 10^7) from standard input. It then calls another function `func_2` with the list `a` as an argument, which returns three values: `s` (the sum of all elements in `a`), `m` (the maximum element in `a`), and `ops` (a list of tuples). The function prints `s` and `m`, followed by each tuple in `ops` with each element incremented by 1. After the function concludes, `n` and `a` retain their initial values, and `s`, `m`, and `ops` are the results of the computation performed by `func_2`.

