#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` and `k` are integers such that 2 <= n <= 40 and 1 <= k <= 2n; `cliques` is the ceiling of `n / k`; `arr` is a list where each segment of length `k` (except possibly the last) is filled with consecutive integers starting from 1; `cliquess` is a list of `n` zeros.
    print(*arr)
    #This is printed: 1 2 3 ... n (where n is the given integer such that 2 <= n <= 40)
    print(cliques)
    #This is printed: Output:
    print(*cliquess)
    #This is printed: 0 0 0 ... 0 (where there are n zeros in total)
#Overall this is what the function does:The function `func_1` takes two integer parameters `n` and `k`, where `n` is between 2 and 40 inclusive, and `k` is between 1 and 2n inclusive. It prints a sequence of integers from 1 to `n`, the number of cliques (which is the ceiling of `n / k`), and a list of `n` zeros. The function does not return any value.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < len(arr), and clique is an integer representing the current clique number.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `arr[left]` to `arr[left + mid - 1]` are set to `small_element`, `small_element + 1`, ..., `small_element + mid - 1` respectively; `cliquess[left]` to `cliquess[left + mid - 1]` are all set to `clique`; all other variables remain unchanged.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `arr[left]` to `arr[left + mid - 1]` are set to `small_element`, `small_element + 1`, ..., `small_element + mid - 1` respectively; `arr[left + mid]` to `arr[left + mid + not_mid - 1]` are set to `big_element`, `big_element - 1`, ..., `big_element - not_mid + 1` respectively; `cliquess[left]` to `cliquess[left + mid + not_mid - 1]` are all set to `clique`; all other variables remain unchanged.
#Overall this is what the function does:The function modifies a portion of the array `arr` between indices `left` and `right`, setting the first half to increasing values starting from `left + 1` and the second half to decreasing values starting from `right + 1`. It also updates the `cliquess` array for the same range, setting all values to the `clique` number.

