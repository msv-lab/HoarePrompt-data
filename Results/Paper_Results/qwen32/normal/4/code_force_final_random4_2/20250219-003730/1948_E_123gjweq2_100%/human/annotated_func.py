#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, and k is an integer such that 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `arr` is a list of length `n` with segments of length `k` (or less for the last segment) filled with values from 1 to `cliques`, and `cliquess` is a list of length `n` with the same segments filled with the same values, except the first segment which is filled with 0.
    print(*arr)
    #This is printed: 1 2 1 2 1 2 1 2 1 2 (where arr is a list of length n with segments of length k filled with values from 1 to cliques)
    print(cliques)
    #This is printed: cliquess (where the first segment is filled with 0s and the subsequent segments are filled with values from 1 to `cliques`)
    print(*cliquess)
    #This is printed: 0 0 ... 0 1 2 ... cliques 1 2 ... cliques ... (where the first segment of 0s has length k or less, and subsequent segments are filled with values from 1 to cliques)
#Overall this is what the function does:The function `func_1` takes two integer parameters, `n` and `k`, where `n` is between 2 and 40 inclusive, and `k` is between 1 and 2n inclusive. It generates two lists, `arr` and `cliquess`, of length `n`. The list `arr` is filled with segments of length `k` (or less for the last segment) with values from 1 to the number of cliques, where the number of cliques is the ceiling of `n / k`. The list `cliquess` is similar to `arr`, but the first segment is filled with 0s. The function prints the list `arr`, the number of cliques, and the list `cliquess`.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < n, and clique is an integer representing the current clique number.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are integers such that \(0 \leq \text{left} < \text{right} < n\), `clique` is an integer representing the current clique number, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is \((\text{right} - \text{left} + 1) // 2\), `not_mid` is \(\text{right} - \text{left} + 1 - \text{mid}\), `arr[left + mid - i - 1]` is `(left + 1) + i` for \(i = 0\) to \(mid - 1\), `cliquess[left + i]` is `clique` for \(i = 0\) to \(mid - 1\).
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `left` and `right` are integers such that \(0 \leq \text{left} < \text{right} < n\), `clique` is an integer representing the current clique number, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is \((\text{right} - \text{left} + 1) // 2\), `not_mid` is \(\text{right} - \text{left} + 1 - \text{mid}\), `arr[left + mid - i - 1]` is `(left + 1) + i` for \(i = 0\) to \(mid - 1\), `cliquess[left + i]` is `clique` for \(i = 0\) to \(mid + not_mid - 1\), `arr[left + mid + i]` is `big_element - i` for \(i = 0\) to `not_mid - 1`, `cliquess[left + mid + i]` is `clique` for \(i = 0\) to `not_mid - 1`.
#Overall this is what the function does:The function `make_array` modifies two lists, `arr` and `cliquess`, based on the input parameters `left`, `right`, and `clique`. It fills a segment of `arr` from index `left` to `right` with a sequence of numbers starting from `left + 1` up to `right + 1`, with the first half in ascending order and the second half in descending order. Simultaneously, it assigns the value of `clique` to the corresponding elements in the `cliquess` list from index `left` to `right`.

