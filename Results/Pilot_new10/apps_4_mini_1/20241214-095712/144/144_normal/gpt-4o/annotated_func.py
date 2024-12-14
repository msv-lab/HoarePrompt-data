#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100000, and a is a list of n positive integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that `1 ≤ n ≤ 100000`, `a` is a sorted list of `n` positive integers, `mex` is the smallest positive integer not represented in the list `a`.
    print(mex)
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `n` positive integers, calculates the smallest positive integer not present in the list, and prints it. It assumes valid input based on predefined constraints.

