#State of the program right berfore the function call: The input includes an integer n where 1 ≤ n ≤ 100,000, and a list of n integers a_1, a_2,..., a_{n} where for each integer a_i, 1 ≤ a_i ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer where 1 ≤ `n` ≤ 100,000, `arr` is a sorted list of `n` integers in ascending order where for each integer `a_i`, 1 ≤ `a_i` ≤ 10^9, and `mex` is the smallest number that is not present in `arr`.
    print(mex)
#Overall this is what the function does:The function accepts an integer n and a list of n integers, sorts the list, and prints the smallest positive integer (starting from 1) that is not present in the sorted list, handling cases where the list may contain duplicates or numbers greater than n, but assuming the input constraints are met.

