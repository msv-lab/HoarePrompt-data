#State of the program right berfore the function call: array is a list of integers representing a permutation of length n (1 ≤ n ≤ 2·10^5), and find is an integer (1 ≤ find ≤ n) that exists in the array. The sum of the lengths of all permutations across all test cases does not exceed 2·10^5.
def func_1(array, find):
    n = len(array)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
        
    #State: `l` is the smallest index such that all elements before `l` are less than `find`, and `r` is the largest index such that all elements after `r` are greater than or equal to `find`. If `find` exists in the array, `l` will be equal to `r + 1` and point to the position just after the last element less than `find`. If `find` does not exist in the array, `l` will be equal to `r + 1` and point to the position where `find` would be inserted to maintain the sorted order.
    if (l != array.index(find)) :
        print(1)
        #This is printed: 1
        return [str(l + 1), str(array.index(find) + 1)]
        #The program returns a list containing two string elements. The first element is the string representation of `l + 1`, and the second element is the string representation of the index of `find` in the array plus one.
    else :
        print(0)
        #This is printed: 0
    #State: `l` is the smallest index such that all elements before `l` are less than `find`, and `r` is the largest index such that all elements after `r` are greater than or equal to `find`. If `find` exists in the array, `l` will be equal to `r + 1` and point to the position just after the last element less than `find`. If `find` does not exist in the array, `l` will be equal to `r + 1` and point to the position where `find` would be inserted to maintain the sorted order. Additionally, `l` is equal to the index of `find` in the array.
#Overall this is what the function does:The function accepts a list of integers `array` representing a permutation and an integer `find` that exists in the array. It returns a list containing two string elements: the first is the string representation of the index of `find` in the array plus one, and the second is also the string representation of the index of `find` in the array plus one. The function prints `1` if the calculated index `l` does not match the index of `find` in the array, otherwise it prints `0`.

