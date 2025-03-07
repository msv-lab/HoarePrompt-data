#State of the program right berfore the function call: No variables are present in the function signature of `func_1`. This function is expected to read input from the standard input, split it into integers, and return them as a map object.
def func_1():
    return map(int, input().split())
    #The program returns a map object containing integers that were read from the standard input and split by whitespace.
#Overall this is what the function does:The function `func_1` reads a line of input from the standard input, splits it into components based on whitespace, converts each component into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: The function `func_2` does not take any parameters. It relies on the output of another function `func_1`, which presumably returns a list.
def func_2():
    return list(func_1())
    #The program returns the list that is the output of `func_1()`
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns the list that is the output of `func_1()`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, k is an integer such that 1 <= k <= n, arr is a list of integers representing the permutation of length n, pos is an integer representing the index of the element k in arr, low and high are integers representing the current search range with the initial values low = 0 and high = n, st is a set used to store the mid values during the binary search process.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is greater than 0, `k` and `arr` are the values returned by `func_1()` and `func_2()` respectively, `low` is 0, `high` is `n`, `st` is a set used to store the mid values during the binary search process, and `pos` is set to the index of `k` in `arr` if `k` is found; otherwise, `pos` remains -1.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `low` is the index of the largest element in `arr` that is less than or equal to `k`, `high` is `low + 1`, `st` is a set containing all the `mid` values calculated during the iterations, and `pos` is the index of `k` in `arr` if `k` is found; otherwise, `pos` remains -1.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: low + 1, pos + 1 (where low is the index of the largest element in arr that is less than or equal to k, and pos is the index of k in arr if k is found; otherwise, pos remains -1)
    #State: `low` is the index of the largest element in `arr` that is less than or equal to `k`, `high` is `low + 1`, `st` is a set containing all the `mid` values calculated during the iterations, and `pos` is the index of `k` in `arr` if `arr[low]` equals `k`; otherwise, `pos` remains -1.
#Overall this is what the function does:The function performs a binary search on a permutation list `arr` to find the largest index where the element is less than or equal to `k`. It prints `0` if `k` is found in the list, otherwise it prints `1` followed by the index of the largest element less than or equal to `k` and the index of `k` if `k` is found.

