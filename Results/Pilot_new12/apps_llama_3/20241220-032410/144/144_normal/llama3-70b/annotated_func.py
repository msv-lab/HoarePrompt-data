#State of the program right berfore the function call: The input is a list of n positive integers, where n is an integer such that 1 <= n <= 100000, and each integer a_i in the list is such that 1 <= a_i <= 10^9.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100000 (inclusive), `arr` is a sorted list of integers, `mex` is the smallest positive integer not present in `arr`.
    print(mex)
#Overall this is what the function does:The function accepts two inputs from the user: an integer `n` representing the number of elements in the list, and a list of `n` positive integers. It sorts the list in ascending order, then calculates and returns the smallest positive integer (mex) that is not present in the sorted list. The function handles lists with any number of elements between 1 and 100000 (inclusive) and integers between 1 and 10^9 (inclusive), and it terminates after printing the mex value. The state of the program after execution is that the sorted list and the calculated mex value are used to determine and print the smallest missing positive integer from the list, covering edge cases such as duplicate integers, single-element lists, and lists without the number 1.

