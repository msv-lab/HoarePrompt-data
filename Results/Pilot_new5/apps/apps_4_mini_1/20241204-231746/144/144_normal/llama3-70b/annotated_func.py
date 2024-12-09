#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a is a list of n positive integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `mex` is the smallest positive integer not present in `arr`, `arr` is a sorted list of `n` positive integers, `n` is a positive integer such that 1 ≤ `n` ≤ 100,000.
    print(mex)
#Overall this is what the function does:The function accepts a positive integer `n` and a list of `n` positive integers. It calculates and prints the smallest positive integer (mex) that is not present in the list. If all integers from 1 to `n` are present, it will print `n + 1` as the smallest missing positive integer. The function does not consider cases where the list is empty or contains non-positive integers, which could lead to unexpected behavior if `n` is not specified correctly in the input.

