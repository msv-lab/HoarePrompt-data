#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, k is an integer such that 1 <= k <= 2 * n, and the function `make_array` is defined elsewhere to fill the array `arr` with values based on the specified range and clique index.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: Output State: `cliques` is at least 1, `i` is `cliques`, `n` is an integer such that 2 <= n <= 40, `k` is an integer such that 1 <= k <= 2 * n, `arr` is a list of `n` ones, `cliquess` is a list of `n` ones.
    #
    #**Explanation:** After the loop completes all its iterations, `i` will be equal to `cliques`. Since the loop increments `i` by 1 in each iteration, and it runs from `0` to `cliques-1`, the final value of `i` will be `cliques`. The loop sets elements in the `arr` and `cliquess` lists based on the value of `i * k` and `min((i + 1) * k - 1, n - 1)`. Given that the loop runs `cliques` times, every index from `0` to `n-1` in the `arr` and `cliquess` lists will be set to `1`, making both lists a list of `n` ones.
    print(*arr)
    #This is printed: 1 1 1 ... 1 (n times)
    print(cliques)
    #This is printed: cliques (where cliques is at least 1)
    print(*cliquess)
    #This is printed: 1 1 1 ... 1 (where there are n ones in the list)
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 2 and 40, and `k` is an integer between 1 and 2 * `n`. It does not return any value. The function calculates the number of cliques (`cliques`) based on `n` and `k`, initializes two arrays `arr` and `cliquess` with `n` ones, and fills these arrays using the `make_array` function. Finally, it prints the contents of `arr`, the number of cliques, and the contents of `cliquess`.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < n, and clique is an integer representing the clique identifier.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: `i` is equal to `mid`, `cliquess[left + mid - 1]` is `clique`, `arr[left + mid - 1]` is `small_element + mid - 1`, `arr[left + mid - 2]` is `small_element + mid - 2`, ..., `arr[left]` is `small_element + mid - 1`.
    #
    #In this final state, after the loop has executed all its iterations, the variable `i` will be equal to `mid`. The array `arr` will have been filled with values starting from `small_element` up to `small_element + mid - 1`, starting from index `left + mid - 1` and moving backwards to `left`. The `cliquess` array will have the value `clique` stored from index `left` to `left + mid - 1`. All other variables remain in their initial or previously unchanged states.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `i` is equal to `mid`, `cliquess[left + mid - 1]` is `clique`, `arr[left + mid - 1]` is `big_element - (mid - 1)`, `arr[left + mid - 2]` is `big_element - (mid - 2)`, ..., `arr[left]` is `big_element - 1`
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. It returns an array `arr` where elements are filled based on the given `left` and `right` indices. Specifically, it fills the array with values ranging from `small_element` to `small_element + mid - 1` in reverse order from the `left + mid - 1` index to the `left` index. It also fills another array `cliquess` with the value `clique` from the `left` index to the `left + mid - 1` index. The remaining elements in both arrays are filled with values from `big_element - (mid - 1)` to `big_element - 1` in ascending order from the `left + mid` index to the `left + not_mid - 1` index.

