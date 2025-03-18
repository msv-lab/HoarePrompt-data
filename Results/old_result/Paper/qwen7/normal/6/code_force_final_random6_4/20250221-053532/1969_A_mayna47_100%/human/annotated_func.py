#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i is an integer such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: Output State: The function has either printed '2' and returned, or it has iterated through all indices from 1 to `n` without finding any `i` such that `v[v[i]] == i`. In the latter case, the function returns `None`.
    #
    #In more detail, the loop will continue to iterate over each index `i` from 1 to `n`. If for any `i`, the condition `v[v[i]] == i` is met, the function prints '2' and immediately returns. If no such `i` is found after checking all indices, the function will complete all iterations and return `None`.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function reads two inputs: the number of elements `n` and a list of `n` integers `p`. It then checks if there exists any index `i` such that the value at index `v[v[i]]` equals `i`. If such an index is found, it prints '2' and returns. If no such index is found after checking all elements, it prints '3' and returns `None`.

