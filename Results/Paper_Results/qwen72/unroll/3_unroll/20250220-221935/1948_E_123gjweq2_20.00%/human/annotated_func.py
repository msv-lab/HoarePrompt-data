#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` and `k` are integers such that 2 <= n <= 40 and 1 <= k <= 2n, `cliques` is the ceiling of `n / k`, `arr` is a list of `n` elements where the first `k` elements are 1, the next `k` elements are 2, and so on, up to the last segment which is set to `cliques`, `cliquess` is a list of `n` zeros.
    print(*arr)
    #This is printed: 1 1 ... [cliques] [cliques] [cliques] (where the first k elements are 1, the next k elements are 2, and so on, up to the last segment which is set to cliques, and cliques is the ceiling of n / k)
    print(cliques)
    #This is printed: cliques (where cliques is the ceiling of \(n / k\))
    print(*cliquess)
    #This is printed: - The output will be a sequence of `n` zeros separated by spaces.
    #
    #Output:
#Overall this is what the function does:The function `func_1` accepts two integer parameters `n` and `k`, where 2 <= n <= 40 and 1 <= k <= 2n. It calculates the number of cliques as the ceiling of `n / k`. The function initializes a list `arr` of length `n` with all elements set to 0. It then assigns a value to each segment of `arr` such that the first `k` elements are set to 1, the next `k` elements are set to 2, and so on, up to the last segment which is set to the calculated number of cliques. The function prints the elements of `arr` separated by spaces, followed by the number of cliques, and finally a sequence of `n` zeros separated by spaces. The function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right, and clique is a positive integer.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` remain non-negative integers such that `left` <= `right`, `clique` remains a positive integer, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left) // 2`, `not_mid` is `right - left + 1 - (right - left) // 2`. The elements in `arr` from index `left` to `left + mid - 1` are set to values from `small_element` to `small_element + mid - 1`, and the elements in `cliquess` from index `left` to `left + mid - 1` are all set to `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: The elements in `arr` from index `left` to `left + mid - 1` are set to values from `small_element` to `small_element + mid - 1`, and the elements in `arr` from index `left + mid` to `right` are set to values from `big_element` to `big_element - (not_mid - 1)`. The elements in `cliquess` from index `left` to `right` are all set to `clique`. The values of `left`, `right`, `clique`, `small_element`, `big_element`, `mid`, and `not_mid` remain unchanged.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. `left` and `right` are non-negative integers with `left` ≤ `right`, and `clique` is a positive integer. The function modifies two external arrays, `arr` and `cliquess`, such that the elements in `arr` from index `left` to `right` are set to a sequence of values starting from `left + 1` and increasing to `left + mid` (where `mid` is `(right - left) // 2`), followed by a sequence of values starting from `right + 1` and decreasing to `right + 1 - (right - left + 1 - mid)`. The elements in `cliquess` from index `left` to `right` are all set to the value of `clique`. The function does not return any value.

