#State of the program right berfore the function call: n and k are integers where 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` and `k` are integers where 2 <= n <= 40 and 1 <= k <= 2n; `cliques` is the smallest integer greater than or equal to `n / k`; `arr` is a list of integers of length `n` with elements from index `i * k` to `min((i + 1) * k - 1, n - 1)` set to `i + 1` for `i` from 0 to `cliques - 1` and other elements initialized to 0; `cliquess` is a list of integers of length `n` with all elements set to `cliques`.
    print(*arr)
    #This is printed: 1 1 1 2 2 2 3 3 3 4
    print(cliques)
    #This is printed: cliques (where cliques is the smallest integer greater than or equal to \( \frac{n}{k} \))
    print(*cliquess)
    #This is printed: cliques cliques ... cliques (repeated n times, where cliques is the smallest integer greater than or equal to n / k)
#Overall this is what the function does:The function `func_1` takes two integer parameters `n` and `k`, where `2 <= n <= 40` and `1 <= k <= 2n`. It prints an array `arr` of length `n` where elements are grouped into `cliques` (the smallest integer greater than or equal to `n / k`), with each group of elements set to a unique integer value starting from 1. It also prints the number of cliques and an array `cliquess` of length `n` where each element is set to the number of cliques.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < n, and clique is an integer representing the clique number.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are integers such that `0 <= left < right < n` and `right - left >= 1`, `clique` is an integer representing the clique number, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left + 1) // 2`, `not_mid` is `(right - left + 1) // 2`, `arr[left + mid - i - 1]` is `left + 1 + i` for `i` in `0` to `mid - 1`, `cliquess[left + i]` is `clique` for `i` in `0` to `mid - 1`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `left` and `right` are integers such that `0 <= left < right < n` and `right - left >= 1`; `clique` is an integer representing the clique number; `small_element` is `left + 1`; `big_element` is `right + 1`; `mid` is `(right - left + 1) // 2`; `not_mid` is `(right - left + 1) // 2`; `arr[left + mid - i - 1]` is `left + 1 + i` for `i` in `0` to `mid - 1`; `cliquess[left + i]` is `clique` for `i` in `0` to `mid - 1`; `arr[left + mid + i]` is `right + 1 - i` for `i` in `0` to `not_mid - 1`; `cliquess[left + mid + i]` is `clique` for `i` in `0` to `not_mid - 1`.
#Overall this is what the function does:The function modifies the `arr` and `cliquess` arrays by filling a segment from index `left` to `right` with specific values. The first half of this segment is filled with increasing values starting from `left + 1`, and the second half with decreasing values starting from `right + 1`. Additionally, it sets the `clique` number for each position in the segment in the `cliquess` array.

