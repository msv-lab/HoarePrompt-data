#State of the program right berfore the function call: array is a list of integers representing a permutation of length n (1 ≤ n ≤ 2·10^5) containing distinct integers from 1 to n, and find is an integer (1 ≤ find ≤ n) that needs to be found in the permutation. The function is called for multiple test cases, with the sum of all n across test cases not exceeding 2·10^5.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: `l` is the smallest index such that all elements at indices less than `l` are less than `find`, and `r` is `l - 1`.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two strings: the first string is the value of `l + 1`, and the second string is the value of the index of the first occurrence of `find` in the array plus 1.
    else :
        print(0)
        #This is printed: 0
    #State: `l` is the smallest index such that all elements at indices less than `l` are less than `find`, and `r` is `l - 1`. Additionally, `l` is equal to the index of `find` in the array.
#Overall this is what the function does:The function accepts a list of integers representing a permutation and an integer to find within that permutation. It returns a list containing two strings: the first string is the position of the smallest element in the list that is not less than the integer to find, and the second string is the position of the integer to find in the list. If the smallest element not less than the integer to find is the integer itself, it prints 0; otherwise, it prints 1.

