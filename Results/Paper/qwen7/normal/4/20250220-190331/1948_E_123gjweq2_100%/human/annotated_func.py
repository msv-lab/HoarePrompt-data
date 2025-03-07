#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, k is an integer such that 1 <= k <= 2 * n, and the function `make_array` is defined elsewhere to fill the array `arr` based on the specified range and clique index.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: Output State: `cliques` must be greater than 0, `i` is equal to `cliques * 2 - 1`, `make_array` is called `cliques` times with arguments `i * k`, `min((i + 1) * k - 1, n - 1)`, and `i + 1`.
    #
    #In this final state, after the loop has executed all its iterations, `i` will be equal to `cliques * 2 - 1` because the loop increments `i` from 0 to `cliques - 1`. The function `make_array` will have been called `cliques` times, each time with the appropriate arguments based on the current value of `i`.
    print(*arr)
    #This is printed: [result of make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1) for i in range(cliques)]
    print(cliques)
    #This is printed: cliques
    print(*cliquess)
    #This is printed: cliquess (where cliquess is a list of length cliques, with each element being the result of make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1) for i ranging from 0 to cliques - 1)
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 2 and 40 inclusive, and `k` is an integer between 1 and 2*n inclusive. It calculates the number of cliques (`cliques`) as `ceil(n / k)`, initializes two arrays `arr` and `cliquess`, and fills `arr` using the `make_array` function based on the specified range and clique index. Finally, it prints the contents of `arr`, the number of cliques, and the contents of `cliquess`.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < n, and clique is an integer representing the clique identifier.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: The loop will execute `mid` times. After all iterations, the following conditions will hold:
    #
    #- `i` will range from `0` to `mid - 1`.
    #- For each `i` in this range, `cliquess[left + i]` will be set to `clique`.
    #- `arr[left + mid - i - 1]` will be set to `small_element + i`.
    #
    #In simpler terms, the `cliquess` array will be filled with `clique` from index `left` to `left + mid - 1`. The `arr` array will have values from `small_element` to `small_element + mid - 1` placed in reverse order starting from index `left + mid - 1` down to `left`.
    #
    #All other variables (`left`, `right`, `clique`, `small_element`, `big_element`, `mid`, `not_mid`) will retain their values from the initial state or previous iterations.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The loop has executed `not_mid` times. After all iterations, the following conditions will hold:
    #
    #- `i` will range from `0` to `not_mid - 1`.
    #- For each `i` in this range, `cliquess[left + mid + i]` will be set to `clique`.
    #- `arr[left + mid + i]` will be set to `big_element - i`.
    #
    #In simpler terms, the `cliquess` array will be filled with `clique` from index `left + mid` to `left + mid + not_mid - 1`. The `arr` array will have values from `big_element - 0` to `big_element - (not_mid - 1)` placed starting from index `left + mid` up to `left + mid + not_mid - 1`.
    #
    #All other variables (`left`, `right`, `clique`, `small_element`, `big_element`, `mid`, `not_mid`) will retain their values from the initial state or previous iterations.
#Overall this is what the function does:The function `make_array` takes two integers `left` and `right` (where `0 <= left < right < n`), and one integer `clique`. It modifies two arrays `arr` and `cliquess` in place. Specifically, it fills a portion of the `cliquess` array with the value `clique` from index `left` to `left + mid - 1` and from `left + mid` to `left + mid + not_mid - 1`, where `mid` and `not_mid` are calculated based on `left`, `right`, `small_element`, and `big_element`. Additionally, it fills a portion of the `arr` array with values ranging from `small_element` to `small_element + mid - 1` in reverse order and from `big_element - (not_mid - 1)` to `big_element` in ascending order. The function does not return anything.

