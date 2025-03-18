#State of the program right berfore the function call: n is an integer such that 2 <= n <= 40, k is an integer such that 1 <= k <= 2 * n, and the function `make_array` is defined elsewhere to fill the array `arr` based on the specified parameters.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: i is cliques; cliques is ceil(n / k); the array is made with values [cliquess[i-1], min(cliquess[i], n - 1), i + 1].
    print(*arr)
    #This is printed: cliques[i-1] min(cliques[i], n - 1) i + 1
    print(cliques)
    #This is printed: ceil(n / k)
    print(*cliquess)
    #This is printed: C C min(C, n - 1) i + 1 (where C is ceil(n / k))
#Overall this is what the function does:The function accepts two parameters `n` and `k`, where `n` is an integer between 2 and 40 inclusive, and `k` is an integer between 1 and 2*n inclusive. It calculates the number of cliques as `ceil(n / k)` and fills an array `arr` using the `make_array` function based on the calculated cliques. The function then prints the filled array `arr`, the number of cliques, and another array `cliquess` containing the clique sizes.

#State of the program right berfore the function call: left and right are integers such that 0 <= left < right < n, and clique is an integer representing the clique identifier.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: All elements in the array `arr` from index `left` to `left + mid - 1` are set to values ranging from `small_element` to `small_element + mid - 1`. The corresponding elements in the `cliquess` array are all set to the value of `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: All elements in the array `arr` from index `left + mid` to `left + mid + not_mid - 1` are set to values ranging from `big_element - (not_mid - 1)` to `big_element - 1`. The corresponding elements in the `cliquess` array are all set to the value of `clique - (not_mid - 1)` to `clique`.
    #
    #In more detail, after the loop has executed all its iterations, the `arr` array will have its elements from index `left + mid` to `left + mid + not_mid - 1` filled with values starting from `big_element - (not_mid - 1)` and decrementing by 1 until `big_element - 1`. Similarly, the `cliquess` array will have its elements from index `left + mid` to `left + mid + not_mid - 1` set to values starting from `clique - (not_mid - 1)` and decrementing by 1 until `clique`.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. It modifies an array `arr` and another array `cliquess` such that the subarray of `arr` from index `left` to `left + mid - 1` contains values ranging from `small_element` to `small_element + mid - 1`, and the subarray from index `left + mid` to `left + mid + not_mid - 1` contains values ranging from `big_element - (not_mid - 1)` to `big_element - 1`. Correspondingly, the subarray of `cliquess` from index `left` to `left + mid - 1` is set to `clique`, and the subarray from index `left + mid` to `left + mid + not_mid - 1` is set to `clique - (not_mid - 1)`.

