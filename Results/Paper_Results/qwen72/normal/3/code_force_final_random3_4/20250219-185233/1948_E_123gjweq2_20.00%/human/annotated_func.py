#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 40 and 1 <= k <= 2n.
def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
        
    #State: `n` and `k` are integers such that 2 <= n <= 40 and 1 <= k <= 2n, `cliques` is the ceiling of `n / k`, `arr` is a list of `n` zeros with elements from index `0` to `n-1` set to their respective clique number (1 to `cliques`), `cliquess` is a list of `n` zeros with elements from index `0` to `n-1` set to their respective clique number (1 to `cliques`), and `i` is `cliques - 1`.
    print(*arr)
    #This is printed: 1 1 1 2 2 2 3 3 3 4 (where the elements are the clique numbers of the respective indices in the list `arr`)
    print(cliques)
    #This is printed: cliques (where cliques is the ceiling of \(n / k\))
    print(*cliquess)
    #This is printed: 1 1 ... 1 2 2 ... 2 3 3 ... 3 ... cliques (where the list has `n` elements, and each element is the respective clique number from 1 to `cliques`)
#Overall this is what the function does:The function `func_1` accepts two integer parameters, `n` and `k`, with the constraints 2 <= n <= 40 and 1 <= k <= 2n. It calculates the number of cliques as the ceiling of `n / k` and assigns each element in two lists, `arr` and `cliquess`, a clique number (from 1 to the number of cliques). The function then prints the elements of `arr`, the number of cliques, and the elements of `cliquess`. The function does not return any value. After the function concludes, `arr` and `cliquess` are lists of length `n` where each element is set to its respective clique number, and the number of cliques is printed.

#State of the program right berfore the function call: left and right are non-negative integers such that left <= right, and clique is a positive integer.
def make_array(left, right, clique):
    small_element = left + 1
    big_element = right + 1
    mid = (big_element - small_element) // 2
    not_mid = right - left + 1 - mid
    for i in range(mid):
        arr[left + i] = small_element + i
        
        cliquess[left + i] = clique
        
    #State: `left` and `right` are non-negative integers such that `left` <= `right` and `right - left` is at least 2, `clique` is a positive integer, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left) // 2`, `not_mid` is `(right - left + 1) - ((right - left) // 2)`, `i` is `mid - 1`, `arr[left + i]` is `left + 1 + i` for all `i` in the range `[0, mid - 1]`, and `cliquess[left + i]` is `clique` for all `i` in the range `[0, mid - 1]`.
    for i in range(not_mid):
        arr[left + mid + i] = big_element - i
        
        cliquess[left + mid + i] = clique
        
    #State: After the loop executes all the iterations, `left` and `right` remain non-negative integers such that `left` <= `right` and `right - left` is at least 2, `clique` remains a positive integer, `small_element` is `left + 1`, `big_element` is `right + 1`, `mid` is `(right - left) // 2`, `not_mid` is `(right - left + 1) - ((right - left) // 2)`, and for all `i` in the range `[0, not_mid - 1]`, `arr[left + mid + i]` is `right + 1 - i` and `cliquess[left + mid + i]` is `clique`.
#Overall this is what the function does:The function `make_array` accepts three parameters: `left`, `right`, and `clique`. It modifies two arrays, `arr` and `cliquess`, such that for the range `[left, right]` in `arr`, the first half (or the first half plus one if the range length is odd) is filled with increasing values starting from `left + 1`, and the second half is filled with decreasing values starting from `right + 1`. The corresponding indices in `cliquess` are all set to the value of `clique`. The function does not return any value.

