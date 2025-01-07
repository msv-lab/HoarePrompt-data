#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 100 000), representing the number of elements in the array. The second line contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9), representing the elements of the array.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `arr` is a list of `n` integers sorted in ascending order with at least one element, `mex` is the smallest positive integer not present in `arr`.
    print(mex)
#Overall this is what the function does:The function reads an integer \( n \) followed by \( n \) integers from the standard input. It then sorts the array of integers in ascending order. After sorting, the function iterates through the array to find the smallest positive integer that is not present in the array. If all integers from 1 to \( n \) are present in the array, the function returns \( n+1 \). The function prints the result to the standard output.

