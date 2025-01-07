#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a is a list of n positive integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a sorted list of `n` positive integers, `mex` is the smallest positive integer not present in the list `a`.
    print(mex)
#Overall this is what the function does:The function reads a positive integer `n`, followed by a list of `n` positive integers. It sorts the list and computes the smallest positive integer (mex) that is not present in the list. Finally, it prints this value of `mex`. The function does not return any value explicitly.

