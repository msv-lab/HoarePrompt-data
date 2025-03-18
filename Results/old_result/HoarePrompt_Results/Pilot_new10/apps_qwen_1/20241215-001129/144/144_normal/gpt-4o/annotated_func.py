#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100 000, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 100,000, `a` is a list of `n` integers sorted in ascending order, and `mex` is the smallest non-negative integer not present in the list `a`.
    print(mex)
#Overall this is what the function does:The function accepts a list of integers `a` of length `n` and prints the smallest non-negative integer that is not present in the list.

