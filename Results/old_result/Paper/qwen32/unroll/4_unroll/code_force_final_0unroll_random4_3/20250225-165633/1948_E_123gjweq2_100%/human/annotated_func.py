#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `arr` and `cliquess` are lists where the first `k` elements are `1`, the next `k` elements are `2`, and so on, with the last block possibly being smaller if `n` is not a multiple of `k`.
    print(*arr)
    #This is printed: 1 1 1 2 2 2 ... up to the nth element, where the elements are grouped in blocks of k with each block containing the same number, and the last block may be smaller if n is not a multiple of k
    print(cliques)
    #This is printed: cliquess (where cliquess is a list constructed such that the first k elements are 1, the next k elements are 2, and so on, with the last block possibly being smaller if n is not a multiple of k)
    print(*cliquess)
    #This is printed: 1 1 1 2 2 2 3 3 3 3 (where each block of k elements contains the same integer, starting from 1 and incrementing by 1 for each subsequent block, with the last block possibly being smaller if n is not a multiple of k)
#Overall this is what the function does:The function `func_1` takes two integer parameters, `n` and `k`, where `n` is between 2 and 40 inclusive, and `k` is between 1 and 2n inclusive. It constructs two lists, `arr` and `cliquess`, where elements are grouped in blocks of size `k`, with each block containing the same integer starting from 1 and incrementing by 1 for each subsequent block. The last block may be smaller if `n` is not a multiple of `k`. The function prints the list `arr`, the number of blocks (cliques), and the list `cliquess`.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < len(arr), and clique is an integer representing the clique number.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are integers such that 0 <= left < right < len(arr), `clique` is an integer representing the clique number; `small_element` is `left + 1`; `big_element` is `right + 1`; `mid` is `(right - left + 1) // 2`; `not_mid` is `right - left + 1 - mid`; `arr[left + mid - 1]` to `arr[left]` are set to values from `small_element` to `small_element + mid - 1`; `cliquess[left]` to `cliquess[left + mid - 1]` are set to `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `arr[left + mid]` to `arr[left + mid + not_mid - 1]` are set to values from `big_element` down to `big_element - not_mid + 1`; `cliquess[left + mid]` to `cliquess[left + mid + not_mid - 1]` are set to `clique`; all other variables (`left`, `right`, `clique`, `small_element`, `big_element`, `mid`, `not_mid`) remain unchanged.
#Overall this is what the function does:The function `make_array` modifies the input array `arr` and `cliquess` by setting specific segments of `arr` to a sequence of increasing and decreasing values based on the `left` and `right` indices, and assigns the `clique` value to the corresponding segment in `cliquess`.

