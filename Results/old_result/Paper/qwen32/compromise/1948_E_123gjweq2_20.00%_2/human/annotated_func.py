#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `arr` is a list with blocks of `k` elements filled with consecutive integers starting from `1` up to `cliques`. `cliquess` is a list of `n` zeros.
    print(*arr)
    #This is printed: 1 2 3 ... (cliques * k) (where each number is separated by a space and cliques * k is the total number of elements in arr)
    print(cliques)
    #This is printed: [0, 0, ..., 0] (where there are n zeros in the list)
    print(*cliquess)
    #This is printed: 0 0 0 ... 0 (where there are n zeros)
#Overall this is what the function does:The function `func_1` takes two integer parameters, `n` and `k`, where `n` is between 2 and 40, and `k` is between 1 and 2n. It initializes an array `arr` of size `n` and fills it with blocks of `k` elements, each block containing consecutive integers starting from 1 up to the number of cliques (`ceil(n / k)`). Another array `cliquess` of size `n` is initialized with zeros. The function prints the filled `arr` array, the number of cliques, and the `cliquess` array which remains unchanged as all zeros.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < len(arr), and clique is an integer representing the clique identifier.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are integers such that 0 <= left < right < len(arr), `clique` is an integer representing the clique identifier, `small_element` is left + 1, `big_element` is right + 1, `mid` is (right - left) // 2, and `not_mid` is (right - left + 2) // 2. Additionally, arr[left] to arr[left + mid - 1] are set to the sequence left + 1 to left + mid, and cliquess[left] to cliquess[left + mid - 1] are set to clique.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `arr[left]` to `arr[left + mid - 1]` are `left + 1` to `left + mid`, `arr[left + mid]` to `arr[left + mid + not_mid - 1]` are `big_element` to `big_element - (not_mid - 1)`, `cliquess[left]` to `cliquess[left + mid + not_mid - 1]` are `clique`.
#Overall this is what the function does:The function `make_array` modifies a portion of the array `arr` from index `left` to `right` (inclusive) by setting the first half to increasing values starting from `left + 1` and the second half to decreasing values starting from `right + 1`. It also assigns the specified `clique` identifier to all elements in the modified portion of `arr`.

