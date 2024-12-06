#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a is a list of n positive integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 10^9.
def func():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    mex = 1
    for num in arr:
        if num == mex:
            mex += 1
        elif num > mex:
            break
        
    #State of the program after the  for loop has been executed: `n` is a positive integer satisfying 1 ≤ `n` ≤ 100,000; `a` is a list of `n` positive integers; `arr` is a sorted list of integers; `mex` is the smallest positive integer not present in `arr`.
    print(mex)
#Overall this is what the function does:The function accepts a positive integer `n` and a list of `n` positive integers, determines the smallest positive integer not present in the list, and prints this value.

