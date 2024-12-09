#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a is a list of n positive integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
        
    #State of the program after the  for loop has been executed: `mex` is equal to the smallest integer greater than the maximum element in `a`, and `a` is a list of `n` positive integers sorted in non-decreasing order.
    print(mex)
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `n` positive integers. It computes and prints the smallest positive integer (mex) that is not present in the list `a`. The mex is defined as the smallest integer greater than the maximum element in `a` if all integers from 1 to that integer are present in the list. The function does not return any value; it only prints the result.

