#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, k is an integer such that 1 <= k <= 2 * n, and the function `make_array` is defined elsewhere to fill the array `arr` based on the given parameters.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: Output State: `i` is equal to the value of `cliques`, `cliques` is the ceiling of `n` divided by `k`, `k` is used in calculations but its value is not defined, the array is made with values from `i * k` to `min((i + 1) * k - 1, n - 1)` for each iteration of `i` from 0 to `cliques - 1`.
    #
    #In this final state, after the loop has executed all its iterations, the variable `i` will be equal to the final value of `cliques`. The array `arr` will have been updated according to the loop's logic, where for each `i` from 0 to `cliques - 1`, it sets elements from index `i * k` to `min((i + 1) * k - 1, n - 1)` to `i + 1`. The exact values in the array will depend on the specific values of `n` and `k`, but it will reflect these updates.
    print(*arr)
    #This is printed: 1 1 1 2 2 2 3 3 3 4
    print(cliques)
    #This is printed: cliques (where cliques is the ceiling of n divided by k)
    print(*cliquess)
    #This is printed: [1, 1, 1, 2, 2, 2, 3, 3, 3, 4] (where the exact values depend on the specific values of n and k, but the pattern is as described)
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 2 and 40, and `k` is an integer between 1 and 2 * `n`. It calculates the number of cliques (`cliques`) as the ceiling of `n` divided by `k`. The function then uses the `make_array` function to fill an array `arr` with values from 0 to `n-1` based on the calculated cliques. After filling the array, it prints the array, the number of cliques, and another array `cliquess` which is set to `[1, 1, ..., 4]` depending on the values of `n` and `k`. The final state of the program includes the printed output of the array, the number of cliques, and the array `cliquess`.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < n, and clique is an integer representing the clique identifier.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: Output State: The loop runs for `mid` iterations. After all iterations, `arr[left + mid - i - 1]` will be set to `small_element + i` for each `i` from `0` to `mid-1`. Additionally, `cliquess[left + i]` will be set to `clique` for each `i` from `0` to `mid-1`. All other variables (`left`, `right`, `clique`, `small_element`, `big_element`, `mid`, and `not_mid`) remain unchanged.
    #
    #In simpler terms, after the loop completes all its iterations, the array `arr` will have elements from `small_element` to `small_element + mid - 1` placed in positions starting from `left + mid - 1` and going backwards to `left`. The list `cliquess` will have the value `clique` assigned to each index from `left` to `left + mid - 1`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: All elements in `cliquess` from index `left + mid` to `left + mid + not_mid - 1` are set to `clique`. All elements in `arr` from index `left + mid` to `left + mid + not_mid - 1` are set to values ranging from `big_element - (not_mid - 1)` to `big_element`.
    #
    #In simpler terms, after the loop completes all its iterations, the array `arr` will have elements from `big_element - (not_mid - 1)` to `big_element` placed in positions starting from `left + mid` and going forwards to `left + mid + not_mid - 1`. The list `cliquess` will have the value `clique` assigned to each index from `left + mid` to `left + mid + not_mid - 1`.
#Overall this is what the function does:The function `make_array` takes three parameters: `left`, `right`, and `clique`. It creates an array where elements from `small_element` to `small_element + mid - 1` are placed in reverse order starting from `left + mid - 1` and going backwards to `left`. The list `cliquess` has the value `clique` assigned to each index from `left` to `left + mid - 1`. Additionally, elements from `big_element - (not_mid - 1)` to `big_element` are placed in order starting from `left + mid` and going forwards to `left + mid + not_mid - 1`. The list `cliquess` also has the value `clique` assigned to each index from `left + mid` to `left + mid + not_mid - 1`. The function modifies the global arrays `arr` and `cliquess` but does not return anything.

