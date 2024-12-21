#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a is a list of n positive integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ `n` ≤ 100,000); `a` is a sorted list of `n` positive integers (1 ≤ `a[i]` ≤ 10^9); `mex` is the smallest positive integer not present in the list `a`.
    print(mex)
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` containing `n` positive integers, which are read from input. It sorts the list `a` and calculates the smallest positive integer (known as the minimum excluded value, or MEX) that is not present in the list `a`. After iterating through the sorted list, it increments the MEX for each number in `a` that is equal to or greater than the current MEX. Finally, the function prints the computed MEX. The function does not return a value, and it specifically handles cases where all integers from 1 up to `n` might be present in the list, thus may return a MEX that is greater than `n`. Edge cases such as repeated numbers and gaps in the sequence of `a` are also correctly handled, ensuring that the function effectively identifies the smallest missing positive integer.

