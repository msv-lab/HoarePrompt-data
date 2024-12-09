#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a is a list of n positive integers where each element a[i] satisfies 1 ≤ a[i] ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 100,000; `arr` is a sorted list of `n` input integers; `mex` is the smallest positive integer not present in `arr`.
    print(mex)
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 100,000) and a list of `n` positive integers. It calculates the smallest positive integer (mex) that is not present in the list. The function sorts the list and iterates through it, incrementing `mex` whenever it finds a number equal to `mex`. If it encounters a number greater than `mex`, the loop breaks. Finally, it prints the value of `mex`.

