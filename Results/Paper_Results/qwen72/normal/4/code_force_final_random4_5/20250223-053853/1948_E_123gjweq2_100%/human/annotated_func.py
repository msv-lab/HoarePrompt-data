#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` and `k` remain the same; `cliques` is the smallest integer greater than or equal to `n / k`; `arr` is a list of `n` elements where each element is the index of the clique it belongs to (1-indexed); `cliquess` remains a list of `n` zeros.
    print(*arr)
    #This is printed: - The output will be the elements of `arr` printed in a space-separated format.
    #
    #Output:
    print(cliques)
    #This is printed: - The `print(cliques)` statement will print the value of `cliques`, which is the smallest integer greater than or equal to `n / k`.
    #
    #Since the exact values of `n` and `k` are not provided, we can't compute the exact numerical value of `cliques`. However, based on the given information, the print statement will output the smallest integer greater than or equal to `n / k`.
    #
    #Output:
    print(*cliquess)
    #This is printed: - The output will be a sequence of `n` zeros separated by spaces.
    #
    #Output:
#Overall this is what the function does:The function `func_1` accepts two integer parameters `n` and `k`, where 2 <= n <= 40 and 1 <= k <= 2n. It calculates the number of cliques as the smallest integer greater than or equal to `n / k`. The function then prints the elements of a list `arr` of length `n`, where each element represents the clique index (1-indexed) to which the corresponding element belongs. It also prints the number of cliques and a list `cliquess` of `n` zeros. The function does not return any value. After the function concludes, `n` and `k` remain unchanged, `arr` contains the clique indices, and `cliquess` remains a list of `n` zeros.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right and (right - left + 1) is the number of elements to be assigned in the array arr. clique is a positive integer representing the clique number to be assigned to the elements in the range [left, right] in the cliquess array.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` remain unchanged. `clique` remains unchanged. `small_element` remains unchanged. `big_element` remains unchanged. `mid` remains unchanged. `not_mid` remains unchanged. The elements in the range [left, left + mid - 1] of the `arr` array are assigned values from `small_element` to `small_element + mid - 1` in increasing order. The elements in the range [left, left + mid - 1] of the `cliquess` array are assigned the value `clique`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: `left` and `right` remain unchanged. `clique` remains unchanged. `small_element` remains unchanged. `big_element` remains unchanged. `mid` remains unchanged. `not_mid` remains unchanged. The elements in the range [left, left + mid - 1] of the `arr` array are assigned values from `small_element` to `small_element + mid - 1` in increasing order. The elements in the range [left + mid, left + mid + not_mid - 1] of the `arr` array are assigned values from `big_element - not_mid + 1` to `big_element` in decreasing order. The elements in the range [left, left + mid - 1] of the `cliquess` array are assigned the value `clique`. The elements in the range [left + mid, left + mid + not_mid - 1] of the `cliquess` array are assigned the value `clique`.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. It modifies the `arr` and `cliquess` arrays such that: 
- The elements in the range `[left, left + mid - 1]` of the `arr` array are assigned values from `small_element` to `small_element + mid - 1` in increasing order.
- The elements in the range `[left + mid, left + mid + not_mid - 1]` of the `arr` array are assigned values from `big_element - not_mid + 1` to `big_element` in decreasing order.
- The elements in the range `[left, right]` of the `cliquess` array are all assigned the value `clique`.
- The parameters `left`, `right`, and `clique` remain unchanged.

