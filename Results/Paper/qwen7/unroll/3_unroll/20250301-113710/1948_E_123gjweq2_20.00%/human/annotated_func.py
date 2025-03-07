#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, k is an integer such that 1 <= k <= 2 * n, and the function `make_array` is defined elsewhere to fill the array `arr` with values based on the specified range and clique index.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: Output State: `cliques` is equal to ceil(`n` / `k`), `n` is an integer such that 2 <= n <= 40, `k` is an integer such that 1 <= k <= 2 * n, `arr` is a list of `n` ones, `cliquess` is a list of `n` zeros.
    #
    #Explanation: The loop iterates from `i = 0` to `i = cliques - 1`. In each iteration, the function `make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)` is called. This function modifies the `arr` list by setting elements from index `i * k` to `min((i + 1) * k - 1, n - 1)` to `i + 1`. Given the constraints on `n` and `k`, the entire `arr` list will eventually be filled with values from `1` to `cliques`, which is equivalent to `1` repeated `n` times since `cliques` is always less than or equal to `n`. The `cliquess` list remains unchanged as it is not modified within the loop.
    print(*arr)
    #This is printed: 1 1 1 ... 1 (n times)
    print(cliques)
    #This is printed: cliques (where cliques is the ceiling of n / k)
    print(*cliquess)
    #This is printed: 0 0 0 ... 0 (n zeros)
#Overall this is what the function does:The function accepts two integers `n` and `k` within specified ranges, calculates the number of cliques as the ceiling of `n` divided by `k`, and uses the `make_array` function to fill an array `arr` with the value `1` repeated `n` times. It then prints the filled array, the calculated number of cliques, and an array of `n` zeros.

#State of the program right berfore the function call: left and right are integers such that left < right and represent the range of indices in the array arr and cliquess to be filled. clique is an integer representing the current clique identifier.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: `left` is an integer, `right` is an integer, `clique` is an integer representing the current clique identifier, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right + 1 - (left + 1)) // 2`, `not_mid` is `right - left + 1 - mid`, `arr` is a list where elements from index `left` to `left + mid - 1` are set to values starting from `small_element` and incremented by 1 for each subsequent index, and `cliquess` is a list where elements from index `left` to `left + mid - 1` are set to the value of `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: `left` is an integer, `right` is an integer, `clique` is an integer representing the current clique identifier, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right + 1 - (left + 1)) // 2`, `not_mid` is `right - left + 1 - mid`, `arr` is a list where elements from index `left` to `left + mid - 1` are set to values starting from `small_element` and incremented by 1 for each subsequent index, and elements from index `left + mid` to `left + not_mid + mid - 1` are set to values starting from `big_element` and decremented by 1 for each subsequent index, `cliquess` is a list where elements from index `left` to `left + mid - 1` are set to the value of `clique`.
#Overall this is what the function does:The function `make_array` takes three parameters: `left`, `right`, and `clique`. It fills a portion of the `arr` and `cliquess` lists with specific values based on the given range defined by `left` and `right`. Specifically, it assigns values starting from `left + 1` up to `right + 1` to `arr` in a symmetric manner around the midpoint of the range, and sets the corresponding elements in `cliquess` to the value of `clique`. The final state of the program includes the updated `arr` and `cliquess` lists within the specified range.

