#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, and k is an integer such that 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` is an integer such that 2 <= n <= 40, `k` is an integer such that 1 <= k <= 2n, `cliques` is the ceiling of `n / k`, `arr` is a list of `n` elements where each segment of `k` consecutive elements is filled with the corresponding clique number (1, 2, ..., `cliques`), `cliquess` is a list of `n` elements where each segment of `k` consecutive elements is filled with the corresponding clique number (1, 2, ..., `cliques`), `i` is `cliques - 1`.
    print(*arr)
    #This is printed: [1 repeated k times, 2 repeated k times, ..., cliques repeated (n - (cliques-1)*k) times] (where cliques is the ceiling of n/k)
    print(cliques)
    #This is printed: cliques (where cliques is the ceiling of n / k)
    print(*cliquess)
    #This is printed: 1 1 1 ... 1 (k times) 2 2 2 ... 2 (k times) ... cliques cliques ... cliques (remainder times if remainder > 0, otherwise cliques-1 cliques ... cliques (k times)) (where each number from 1 to cliques appears k times, filling up to n elements)
#Overall this is what the function does:The function `func_1` accepts two integer parameters, `n` and `k`, where `n` is between 2 and 40 inclusive, and `k` is between 1 and `2n` inclusive. It calculates the ceiling of `n / k` to determine the number of cliques. The function then creates two lists, `arr` and `cliquess`, each of length `n`, and fills them with numbers representing the clique to which each index belongs, with each clique number repeated up to `k` times. Finally, it prints the list `arr`, the number of cliques, and the list `cliquess`.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < len(arr), and clique is an integer representing the clique number to which the vertices in the range [left, right] will be assigned.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are integers such that `0 <= left < right < len(arr)` and `right - left >= 2`; `clique` is an integer; `small_element` is `left + 1`; `big_element` is `right + 1`; `mid` is `(right - left) // 2`; `not_mid` is `right - left + 1 - (right - left) // 2`; `arr[left + i]` is `(left + 1) + i` for `i` in `[0, mid)`; `cliquess[left + i]` is `clique` for `i` in `[0, mid)`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `left` and `right` are integers such that `0 <= left < right < len(arr)` and `right - left >= 2`; `clique` is an integer; `small_element` is `left + 1`; `big_element` is `right + 1`; `mid` is `(right - left) // 2`; `not_mid` is `right - left + 1 - (right - left) // 2`; `arr[left + i]` is `(left + 1) + i` for `i` in `[0, mid)`; `cliques[left + i]` is `clique` for `i` in `[0, mid)`; `arr[left + mid + i]` is `big_element - i` for `i` in `[0, not_mid)`; `cliquess[left + mid + i]` is `clique` for `i` in `[0, not_mid)`; `i` is `not_mid - 1`.
#Overall this is what the function does:The function `make_array` modifies a portion of the array `arr` by assigning values from `left + 1` to `right + 1` in a specific pattern to the elements in the range from `left` to `right` (inclusive). It also assigns the given `clique` number to each element in this range in the array `cliquess`.

