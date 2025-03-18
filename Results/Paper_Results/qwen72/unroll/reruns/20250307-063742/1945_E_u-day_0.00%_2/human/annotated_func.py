#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return map(int, input().split())
    #The program returns a map object that converts each element from the input string, split by spaces, into an integer.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads a line of input from the user, splits the input string by spaces, and returns a map object that converts each split element into an integer. The final state of the program after the function concludes is that the map object is available for further processing, such as conversion to a list or iteration.

#State of the program right berfore the function call: None, as `func_2` does not take any parameters. However, it assumes that `func_1` returns a list of valid operations (each operation being a pair of indices) that can be used to rearrange the permutation to allow binary search to find the number `x`.
def func_2():
    return list(func_1())
    #The program returns a list of valid operations (each operation being a pair of indices) that can be used to rearrange the permutation to allow binary search to find the number `x`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It returns a list of valid operations, where each operation is a pair of indices, that can be used to rearrange a permutation to allow binary search to find the number `x`. The function assumes that `func_1` provides the necessary list of operations. After the function concludes, the returned list can be used to rearrange the permutation to enable binary search for the number `x`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, k is an integer such that 1 <= k <= n representing the number to be found, and arr is a list of integers representing the permutation of size n.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `pos` is the index of the first occurrence of `k` in `arr`, or -1 if `k` is not found in `arr`.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `pos` remains unchanged, `low` is the largest index such that `arr[low] <= k`, `high` is the smallest index such that `arr[high] > k`, and `st` contains all the midpoints calculated during the loop execution.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: high, pos + 1 (where high is the smallest index such that `arr[high] > k` and pos is the unchanged value of `pos`)
    #State: *`pos` remains unchanged, `low` is the largest index such that `arr[low] <= k`, `high` is the smallest index such that `arr[high] > k`, and `st` contains all the midpoints calculated during the loop execution. Additionally, if `arr[low]` is equal to `k`, then `arr[low]` is `k`. Otherwise, `arr[low]` is not equal to `k`.
#Overall this is what the function does:The function `func_3` does not accept any parameters directly but relies on the outputs of `func_1` and `func_2` to determine the length of the permutation `n`, the number to be found `k`, and the permutation list `arr`. It searches for the first occurrence of `k` in `arr` and stores the index in `pos` (or -1 if `k` is not found). It then performs a binary search to find the largest index `low` such that `arr[low] <= k` and the smallest index `high` such that `arr[high] > k`. If `k` is found at `arr[low]`, it prints `0`. If `k` is not found, it prints `1` followed by the indices `low + 1` and `pos + 1`. The final state of the program includes `pos` (unchanged), `low` (the largest index such that `arr[low] <= k`), `high` (the smallest index such that `arr[high] > k`), and a set `st` containing all midpoints calculated during the binary search.

