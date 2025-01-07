#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100 000, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
        
    #State of the program after the  for loop has been executed: `a` is a sorted list of `n` integers where each integer \(a_i\) satisfies \(1 \leq a_i \leq 10^9\), `n` is an integer such that \(1 \leq n \leq 100,000\), `mex` is the smallest integer greater than any element in the list `a`.
    print(mex)
#Overall this is what the function does:The function takes no explicit parameters but reads two inputs from the standard input: an integer `n` representing the size of the list, and a list of `n` integers `a`. It then sorts the list `a` in ascending order and calculates the smallest non-negative integer (mex) that is not present in the list. The function outputs this value `mex`. The final state of the program includes the variable `mex` being the smallest integer not present in the sorted list `a`. Potential edge cases include when the list `a` contains only one element, or when the list `a` already contains all integers from 1 to `n`. The function also handles the case where the input list `a` is empty, although this case is not explicitly covered in the provided annotations.

