#State of the program right berfore the function call: No variables in the function signature. The function `func_1` is expected to read input from standard input, split it by spaces, and return the resulting values as integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains integers obtained by splitting the input string by spaces.
#Overall this is what the function does:The function `func_1` reads a line of input from standard input, splits it by spaces, and returns a map object containing the resulting values as integers.

#State of the program right berfore the function call: The function `func_2` does not take any parameters. It relies on the output of another function `func_1`, which is expected to return a list.
def func_2():
    return list(func_1())
    #The program returns the list that `func_1` returns
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the result of calling `func_1`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is a positive integer such that 1 <= k <= n.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` and `k` are the values returned by `func_1()`, `arr` is the value returned by `func_2()`, `pos` is the index of the first occurrence of `k` in `arr` or -1 if `k` is not found in `arr`.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `low` and `high` are consecutive indices, and `st` contains all the midpoints calculated during the loop iterations.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: low + 1, pos + 1 (where low is an index in the array `arr` and pos is an index or position used in the context of the loop)
    #State: `low` and `high` are consecutive indices, and `st` contains all the midpoints calculated during the loop iterations. If `arr[low]` equals `k`, then `arr[low]` is equal to `k`. Otherwise, `arr[low]` is not equal to `k`.
#Overall this is what the function does:The function determines the position of a given integer `k` in a permutation array of length `n` and prints specific values based on whether `k` is found at a certain position. It prints `0` if `arr[low]` equals `k`, otherwise it prints `1` followed by `low + 1` and `pos + 1`, where `pos` is the index of the first occurrence of `k` in `arr` or `-1` if `k` is not found.

