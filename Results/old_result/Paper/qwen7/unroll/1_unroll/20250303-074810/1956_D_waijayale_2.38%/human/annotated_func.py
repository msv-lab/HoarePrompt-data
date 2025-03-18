#State of the program right berfore the function call: a is a list of non-negative integers, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list used to store the operations performed.
def func_1(a, l, r, ops):
    if (l == r) :
        if (a[l] != 0) :
            ops.append((l, l))
            a[l] = 0
        #State: Postcondition: `a` is a list of non-negative integers, `l` is equal to `r`, and if the element at index `r` (which is `l`) is not 0, then `ops` is a list containing the tuple `(l, l)`. If the element at index `r` is 0, no change is made to `ops`.
        return
        #The program does not return any value since there is no return statement in the provided code.
    #State: a is a list of non-negative integers, l and r are integers such that 1 <= l <= r <= len(a), and ops is a list used to store the operations performed. The values of l and r are different (i.e., l != r)
    func_1(a, l + 1, r, ops)
    if (a[l] != r - l + 1) :
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `a` is a list where each element from index `l` to index `r` (inclusive) is set to `r - l + 1`. The values of `l` and `r` remain unchanged, with `l` being `l + 1` and `r` being `r`.
        func_1(a, l + 1, r, ops)
    #State: Postcondition: `a` is a list of non-negative integers, `l` and `r` are indices of the list. If `a[l]` is not equal to `r - l + 1`, then each element from index `l + 1` to index `r` (inclusive) in `a` is set to `r - (l + 1) + 1`, and the values of `l` and `r` are updated to `l + 1` and `r` respectively. If `a[l]` is equal to `r - l + 1`, no changes are made to the elements of `a` within the range `[l, r]`.
#Overall this is what the function does:The function processes a list of non-negative integers `a` by adjusting its elements within a specified range `[l, r]` based on certain conditions. If `l` equals `r`, it checks if the element at index `r` is zero; if so, it records an operation. Otherwise, it sets the element at index `r` to zero and records an operation. If `l` is less than `r`, it recursively calls itself with an incremented left boundary. It then checks if the element at index `l` matches the expected value (`r - l + 1`). If not, it updates all elements in the range `[l, r]` to this value and records an operation. This process continues until the entire list is processed according to the specified rules.

#State of the program right berfore the function call: a is a list of non-negative integers, and n is the length of the list such that 1 <= n <= 18.
def func_2(a):
    n = len(a)
    ops = []
    recursive_maximize_sum(0, n - 1)
    return sum(a), len(ops), ops
    #The program returns the sum of all elements in list 'a', the length of list 'ops', and the empty list 'ops' itself.
#Overall this is what the function does:The function accepts a list `a` of non-negative integers and returns the sum of all elements in the list, the length of the operations performed (stored in `ops`), and the empty list `ops` itself.

#State of the program right berfore the function call: a is a list of n integers where 1 <= n <= 18 and 0 <= a_i <= 10^7. l and r are integers such that 1 <= l <= r <= n. ops is a list that will store the operations performed.
def recursive_maximize_sum(l, r):
    s = sum(a[l:r + 1])
    if (s <= (r - l + 1) * (r - l + 1)) :
        func_1(a, l, r, ops)
        ops.append((l, r))
        for i in range(l, r + 1):
            a[i] = r - l + 1
            
        #State: Output State: `ops` is a list containing the sum `s`, `a` is a list where each element from index `l` to index `r` is set to `r - l + 1`, and the other elements of `a` remain unchanged. `l` and `r` retain their original values, and `s` is less than or equal to `(r - l + 1) * (r - l + 1)`.
    else :
        mx = max(a[l:r + 1])
        pos = a[l:r + 1].index(mx) + l
        if (pos != l) :
            recursive_maximize_sum(l, pos - 1)
        #State: `ops` now contains one more element which is the sum `s`; `a`, `l`, and `r` retain their original values; `mx` is the maximum value in the sublist `a[l:r + 1]`; `pos` is the index of `mx` in the sublist `a[l:r + 1]` plus `l`. If `pos` is not equal to `l`, the function `recursive_maximize_sum(l, pos - 1)` has been called.
        if (pos != r) :
            recursive_maximize_sum(pos + 1, r)
        #State: Postcondition: `ops` now contains one more element which is the sum `s`; `a`, `l`, and `r` retain their original values; `mx` is the maximum value in the sublist `a[l:r + 1]`; `pos` is the index of `mx` in the sublist `a[l:r + 1]` plus `l`. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called.
    #State: Postcondition: `ops` is a list that now contains one more element which is the sum `s`. `a` is a list where either each element from index `l` to index `r` is set to `r - l + 1`, and the other elements of `a` remain unchanged, or `a`, `l`, and `r` retain their original values. Additionally, `mx` is the maximum value in the sublist `a[l:r + 1]`, and `pos` is the index of `mx` in the sublist `a[l:r + 1]` plus `l`. If `pos` is not equal to `r`, the function `recursive_maximize_sum(pos + 1, r)` has been called.
#Overall this is what the function does:The function `recursive_maximize_sum` takes two parameters `l` and `r`, which define a range within a list `a`. It modifies the list `a` by setting each element from index `l` to index `r` to `r - l + 1` if the sum of the sublist is less than or equal to `(r - l + 1) * (r - l + 1)`. Otherwise, it finds the maximum value in the sublist and recursively calls itself on the left and right sublists excluding the position of the maximum value. The function does not return a value but updates the list `a` and maintains a list `ops` containing the sums of the processed sublists.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 18, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 10^7.
def func_3():
    n = int(input())
    a = list(map(int, input().split()))
    s, m, ops = func_2(a)
    print(s, m)
    #This is printed: s, m (where s and m are the return values of func_2(a))
    for (l, r) in ops:
        print(l + 1, r + 1)
        
    #State: The numbers `l+1` and `r+1` printed for each operation in `ops`.
#Overall this is what the function does:The function reads an integer `n` and a list `a` of `n` integers from the user. It then calls another function `func_2` with the list `a`, which returns three values: `s`, `m`, and `ops`. The function prints `s` and `m`, and for each operation in `ops`, it prints the indices `l+1` and `r+1`. After completing these actions, the function concludes without returning any value.

