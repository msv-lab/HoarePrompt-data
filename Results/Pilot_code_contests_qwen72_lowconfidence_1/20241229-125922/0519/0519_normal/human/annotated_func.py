#State of the program right berfore the function call: a is a list of integers where 1 ≤ len(a) ≤ 100,000 and 0 ≤ ai ≤ 100,000, p and r are non-negative integers such that 0 ≤ p ≤ r < len(a).
def func_1(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
        
    #State of the program after the  for loop has been executed: `a` is a list of integers where \(1 \leq \text{len}(a) \leq 100,000\) and \(0 \leq a_i \leq 100,000\). `p` and `r` are non-negative integers such that \(0 \leq p \leq r < \text{len}(a)\). `x` is equal to `a[r]`. After the loop, all elements `a[p]` to `a[i]` are less than or equal to `x`, and all elements `a[i+1]` to `a[r-1]` are greater than `x`. `i` is the index of the last element in the segment from `a[p]` to `a[r-1]` that is less than or equal to `x`.
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1
    #The program returns the index `i + 1`, where `i` is the index of the last element in the segment from `a[p]` to `a[r-1]` that is less than or equal to `x`. The value `x` is originally `a[r]`, and after the operation, `a[i + 1]` is equal to `x`, and `a[r]` is equal to the original value of `a[i + 1]`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `a` and two non-negative integers `p` and `r` where `0 ≤ p ≤ r < len(a)`. It partitions the sublist `a[p:r+1]` such that all elements less than or equal to `a[r]` (the pivot) are moved to the left of the pivot, and all elements greater than the pivot are moved to the right. The function then places the pivot in its correct position within the sorted sublist and returns the index of the pivot. The final state of the list `a` is such that `a[p:i+1]` contains elements less than or equal to the pivot, and `a[i+2:r+1]` contains elements greater than the pivot, where `i + 1` is the returned index. The pivot element, originally at `a[r]`, is now at `a[i + 1]`. Edge cases include when `p == r` (the sublist contains only one element), in which case the function returns `r`, and when all elements in the sublist are equal to the pivot, in which case the function still correctly partitions the list and returns the appropriate index.

