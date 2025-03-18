#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: - `n` and `k` remain the same.
    #   - `cliques` remains the same.
    #   - `arr` is modified such that it is divided into `cliques` segments, each filled with a unique value from 1 to `cliques`.
    #   - `cliquess` remains a list of `n` zeros.
    #
    #Output State:
    print(*arr)
    #This is printed: 1 1 ... 1 2 2 ... 2 3 3 ... 3 ... c c ... c (where each segment contains \(\frac{n}{c}\) elements with values from 1 to \(c\))
    print(cliques)
    #This is printed: cliques (where cliques is the number of segments `arr` is divided into, each filled with a unique value from 1 to `cliques`)
    print(*cliquess)
    #This is printed: 0 0 0 ... 0 (a sequence of n zeros separated by spaces)
#Overall this is what the function does:The function `func_1` accepts two integer parameters, `n` and `k`, where 2 <= n <= 40 and 1 <= k <= 2n. It divides the array `arr` of length `n` into `cliques` segments, where `cliques` is the ceiling of `n / k`. Each segment is filled with a unique value from 1 to `cliques`. The function prints the modified array `arr`, the number of segments `cliques`, and a list `cliquess` of `n` zeros. The parameters `n` and `k` remain unchanged, and the function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right and represent the range of indices in the arrays arr and cliquess. clique is a positive integer representing the clique number to be assigned to the vertices in the specified range.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: The elements in `arr` from index `left + mid - 1` to `left` are set to values from `small_element` to `small_element + mid - 1`. The elements in `cliques` from index `left` to `left + mid - 1` are set to `clique`. The values of `left`, `right`, `clique`, `small_element`, `big_element`, `mid`, and `not_mid` remain unchanged.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The elements in `arr` from index `left + mid` to `left + mid + not_mid - 1` are set to values from `big_element - not_mid + 1` to `big_element`. The elements in `cliques` from index `left + mid` to `left + mid + not_mid - 1` are set to `clique`. The values of `left`, `right`, `clique`, `small_element`, `big_element`, `mid`, and `not_mid` remain unchanged.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. It modifies two arrays, `arr` and `cliquess`, such that the elements in `arr` from index `left` to `right` (inclusive) are set to a sequence of integers starting from `left + 1` and ending at `right + 1`. The elements in `cliquess` from index `left` to `right` (inclusive) are set to the value of `clique`. The function does not return any value. After the function concludes, the arrays `arr` and `cliquess` are updated, and the input parameters `left`, `right`, and `clique` remain unchanged.

