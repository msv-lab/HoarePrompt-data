#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` and `k` remain unchanged; `cliques` remains the ceiling of `n / k`; `arr` is divided into segments of size `k`, and each segment is filled with a different integer starting from 1 and increasing by 1 for each subsequent segment. If the last segment is smaller than `k`, it will be filled with the last integer value; `cliquess` remains a list of `n` zeros.
    print(*arr)
    #This is printed: 1 1 1 2 2 2 3 3 3 4 (where the elements of `arr` are constructed based on the given rules and `n` and `k` are the provided values)
    print(cliques)
    #This is printed: cliques (where cliques is the ceiling of n / k)
    print(*cliquess)
    #This is printed: - The `print` statement will print `n` zeros separated by spaces.
    #
    #Output:
#Overall this is what the function does:The function `func_1` accepts two integer parameters `n` and `k`, where `2 <= n <= 40` and `1 <= k <= 2n`. It calculates the number of cliques as the ceiling of `n / k` and divides the array `arr` of length `n` into segments of size `k`, filling each segment with a different integer starting from 1 and increasing by 1 for each subsequent segment. If the last segment is smaller than `k`, it will be filled with the last integer value. The function prints the contents of `arr`, the number of cliques, and a list of `n` zeros. The function does not return any value. After the function concludes, `n` and `k` remain unchanged, `arr` is modified as described, and `cliquess` remains a list of `n` zeros.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right and represent the bounds of a subarray in arr. clique is a positive integer representing the clique number to be assigned to elements in the subarray.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element + 1) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + mid - i - 1] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: The subarray `arr[left:left + mid]` is filled with values starting from `small_element` and increasing by 1 for each subsequent element. The subarray `cliquess[left:left + mid]` is filled with the value `clique`. The values of `left`, `right`, `small_element`, `big_element`, `mid`, and `not_mid` remain unchanged.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: Output State: The subarray `arr[left:left + mid]` is filled with values starting from `small_element` and increasing by 1 for each subsequent element. The subarray `arr[left + mid:left + mid + not_mid]` is filled with values starting from `big_element` and decreasing by 1 for each subsequent element. The subarray `cliquess[left:left + mid]` is filled with the value `clique`. The subarray `cliquess[left + mid:left + mid + not_mid]` is also filled with the value `clique`. The values of `left`, `right`, `small_element`, `big_element`, `mid`, and `not_mid` remain unchanged.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. It modifies two external arrays, `arr` and `cliquess`, such that the subarray `arr[left:right + 1]` is filled with values in a specific pattern. The first half of the subarray (from `left` to `left + mid - 1`) is filled with values starting from `left + 1` and increasing by 1, while the second half (from `left + mid` to `right`) is filled with values starting from `right + 1` and decreasing by 1. The subarray `cliquess[left:right + 1]` is filled entirely with the value `clique`. The function does not return any value.

