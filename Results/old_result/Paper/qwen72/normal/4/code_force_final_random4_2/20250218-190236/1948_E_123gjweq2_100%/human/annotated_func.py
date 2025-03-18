#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` and `k` are integers such that 2 <= n <= 40 and 1 <= k <= 2n, `cliques` is the ceiling of `n / k` and must be equal to the number of times the loop executed, `i` is `cliques - 1`, `arr` is a list of `n` zeros, `cliquess` is a list of `n` zeros, `make_array` is called with arguments (`(cliques - 1) * k`, `min(cliques * k - 1, n - 1)`, `cliques`).
    print(*arr)
    #This is printed: A list of `n` elements, where elements from index \((\text{cliques} - 1) \times k\) to \(\min(\text{cliques} \times k - 1, n - 1)\) are non-zero, and the rest are zeros.
    print(cliques)
    #This is printed: - Since the exact values of `n` and `k` are not provided, we can't compute the exact numerical value of `cliques`. However, based on the given constraints and the formula, the print statement will output the ceiling of \(n / k\).
    #
    #Output:
    print(*cliquess)
    #This is printed: 0 0 ... 0 [cliques] [cliques] ... [cliques] (where the number of 0s is \((cliques - 1) * k\) and the number of [cliques] is \(\min(cliques * k - 1, n - 1) - (cliques - 1) * k + 1\))
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` is an integer between 2 and 40 (inclusive), and `k` is an integer between 1 and 2n (inclusive). It calculates the number of cliques as the ceiling of `n / k`. The function initializes two lists, `arr` and `cliquess`, each of length `n` with all elements set to 0. It then calls the `make_array` function for each clique, which modifies the `arr` list by setting specific elements to non-zero values. After the loop, the function prints the `arr` list, which contains non-zero values in a specific range based on the number of cliques and the value of `k`. It also prints the number of cliques. Finally, it prints the `cliquess` list, which remains unchanged (all elements are 0). The function does not return any value.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right, and clique is a positive integer.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are non-negative integers such that `left` <= `right` and `right - left` >= 1, `mid` is greater than or equal to the number of iterations, `i` is `mid - 1`, `arr[left + mid - 1]` to `arr[left]` are assigned the values `small_element` to `small_element + mid - 1` respectively, `cliquess[left]` to `cliquess[left + mid - 1]` are all assigned the value `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: `left` and `right` are non-negative integers such that `left` <= `right` and `right - left` >= 1, `mid` is greater than or equal to the number of iterations, `i` is `not_mid - 1`, `not_mid` must be greater than or equal to the number of iterations, `arr[left + mid - 1]` to `arr[left]` are assigned the values `small_element` to `small_element + mid - 1` respectively, `cliquess[left]` to `cliquess[left + mid - 1]` are all assigned the value `clique`, `arr[left + mid]` to `arr[left + mid + not_mid - 1]` are assigned the values `big_element` to `big_element - not_mid + 1` respectively, `cliquess[left + mid]` to `cliquess[left + mid + not_mid - 1]` are all assigned the value `clique`.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. `left` and `right` are non-negative integers with `left` ≤ `right`, and `clique` is a positive integer. The function modifies two arrays, `arr` and `cliquess`, such that the elements in `arr` from index `left` to `right` are filled with a sequence of integers. The first half of this range (from `left + mid - 1` to `left`) is filled with values starting from `left + 1` and increasing by 1, while the second half (from `left + mid` to `right`) is filled with values starting from `right + 1` and decreasing by 1. All elements in the `cliquess` array from index `left` to `right` are set to the value of `clique`. The function does not return any value.

