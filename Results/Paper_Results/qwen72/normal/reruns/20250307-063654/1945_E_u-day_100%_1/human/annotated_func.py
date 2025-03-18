#State of the program right berfore the function call: No input variables are present in the function signature.
def func_1():
    return map(int, input().split())
    #The program returns an iterator that converts each element from the input string, split by spaces, into an integer.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an iterator that converts each element from the input string, split by spaces, into an integer. The input string is read from the standard input. After the function concludes, the program has an iterator that can be used to iterate over the converted integers.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It returns a list that is the result of calling the function `func_1()`. After the function concludes, the program has a list containing the elements returned by `func_1()`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, k is a positive integer such that 1 <= k <= n representing the number to be found, and arr is a list of n distinct integers from 1 to n representing the permutation.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is greater than 0, `i` is `n-1`, `k` is updated to the value returned by `func_1()`, `arr` is a list of `n` distinct integers from 1 to `n` representing the permutation and is updated to the value returned by `func_2()`. If `k` is found in `arr`, `pos` is set to the index of `k` in `arr`. Otherwise, `pos` remains -1.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `n` is greater than 1, `i` is `n-1`, `k` is the value returned by `func_1()`, `arr` is a list of `n` distinct integers from 1 to `n` representing the permutation and is updated to the value returned by `func_2()`. If `k` is found in `arr`, `pos` is set to the index of `k` in `arr`. Otherwise, `pos` remains -1. `low` is the index of the largest element in `arr` that is less than or equal to `k`, `high` is the index of the smallest element in `arr` that is greater than `k`, and `st` is a set containing all the midpoints calculated during the loop execution.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: - `low + 1` will be the index of the largest element in `arr` that is less than `k`, incremented by 1.
        #   - `pos + 1` will be -1 + 1, which is 0.
        #
        #Output:
    #State: *`n` is greater than 1, `i` is `n-1`, `k` is the value returned by `func_1()`, `arr` is a list of `n` distinct integers from 1 to `n` representing the permutation and is updated to the value returned by `func_2()`. If `k` is found in `arr`, `pos` is set to the index of `k` in `arr`. Otherwise, `pos` remains -1. `low` is the index of the largest element in `arr` that is less than or equal to `k`, and `high` is the index of the smallest element in `arr` that is greater than `k`. `st` is a set containing all the midpoints calculated during the loop execution. If `arr[low]` is equal to `k`, `pos` is set to `low`. If `arr[low]` is not equal to `k`, `pos` remains -1.
#Overall this is what the function does:The function `func_3` does not accept any parameters directly but calls `func_1` to get `n` and `k`, and `func_2` to get `arr`. It then searches for the integer `k` in the permutation list `arr`. If `k` is found, it sets `pos` to the index of `k` in `arr`. The function also performs a binary search to determine the position of `k` in the sorted list `arr`. If `k` is found in `arr`, it prints `0`. If `k` is not found, it prints `1` followed by the index of the largest element in `arr` that is less than `k` (incremented by 1) and the value `0` (since `pos` remains -1 and is incremented by 1). The final state of the program includes `pos` being set to the index of `k` if `k` is found, otherwise `pos` remains -1. The set `st` contains all the midpoints calculated during the binary search, and `low` and `high` are the indices of the largest and smallest elements in `arr` that are less than or equal to and greater than `k`, respectively.

