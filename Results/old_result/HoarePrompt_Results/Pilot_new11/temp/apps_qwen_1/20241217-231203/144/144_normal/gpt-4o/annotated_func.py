#State of the program right berfore the function call: The input is a list of integers representing the array elements, where the length of the list is between 1 and 100,000 (inclusive), and each element is between 1 and 10^9 (inclusive).
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
        
    #State of the program after the  for loop has been executed: `a` is a non-empty list of integers, `n` is an integer, and `mex` is the smallest non-negative integer not present in `a`.
    print(mex)
#Overall this is what the function does:The function `func` accepts a list of integers and sorts the list in ascending order. It then determines the smallest non-negative integer that is not present in the sorted list. The function prints this integer, which represents the minimum excluded number (Mex) of the list. The function does not return any value; it only prints the result. Potential edge cases include empty lists, lists with duplicate numbers, and lists with consecutive numbers starting from 1.

