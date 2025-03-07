#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, and k is an integer such that 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` is an integer such that 2 <= n <= 40, `k` is an integer such that 1 <= k <= 2n, `cliques` is the smallest integer greater than or equal to `n / k`, `arr` is a list of length `n` where each segment of length `k` or less is filled with consecutive integers starting from 1 up to `cliques`, `cliquess` is a list of length `n` with all elements set to 0.
    print(*arr)
    #This is printed: 1 2 3 ... cliques 1 2 3 ... (cycling through numbers from 1 to cliques in segments of length k until the list reaches the length of n)
    print(cliques)
    #This is printed: Output:
    print(*cliquess)
    #This is printed: 0 (repeated n times)
#Overall this is what the function does:The function `func_1` takes two integer parameters, `n` and `k`, where `n` is between 2 and 40 inclusive, and `k` is between 1 and 2n inclusive. It constructs a list `arr` of length `n` where each segment of length `k` or less is filled with consecutive integers starting from 1 up to the smallest integer greater than or equal to `n / k`. Another list `cliquess` of length `n` with all elements set to 0 is also created. The function prints the list `arr`, the smallest integer greater than or equal to `n / k`, and the list `cliquess`. The function does not return any value explicitly.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < len(arr), and clique is an integer representing the clique number to which the vertices in the range [left, right] will be assigned.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `arr` has elements from index `left + mid - 1` to `left` set to values from `small_element` to `small_element + mid - 1`; `cliquess` has elements from index `left` to `left + mid - 1` set to `clique`; `right`, `big_element`, `mid`, `not_mid` remain unchanged.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `arr` has elements from index `left + mid - 1` to `left` set to values from `small_element` to `small_element + mid - 1`; elements from index `left + mid` to `left + mid + not_mid - 1` set to values from `big_element` to `big_element - not_mid + 1`. `cliquess` has elements from index `left` to `left + mid + not_mid - 1` set to `clique`. `right`, `big_element`, `mid`, `not_mid` remain unchanged.
#Overall this is what the function does:The function `make_array` modifies the array `arr` by assigning specific values to elements in the range from index `left` to `right` (inclusive). It sets the first half of this range to increasing values starting from `left + 1` and the second half to decreasing values starting from `right + 1`. Additionally, it assigns the value of `clique` to each element in the `cliquess` array within the same range.

