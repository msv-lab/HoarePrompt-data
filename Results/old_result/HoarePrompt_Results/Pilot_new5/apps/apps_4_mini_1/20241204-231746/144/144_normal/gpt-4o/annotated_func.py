#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a is a list of n positive integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100,000), `a` is a sorted list of `n` positive integers, `mex` is the smallest positive integer not present in the list `a`, and if `mex` reaches a value greater than `n`, then it will be `n + 1` (indicating all integers from 1 to `n` are present in the list).
    print(mex)
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `n` positive integers. It calculates the smallest positive integer (mex) that is not present in the list `a`. After processing the inputs, it returns the value of `mex`, which can range from 1 to `n + 1`, depending on whether all integers from 1 to `n` are in the list. If all integers from 1 to `n` are present, it returns `n + 1`.

