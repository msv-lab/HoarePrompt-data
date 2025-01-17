#State of the program right berfore the function call: n is an integer representing the upper limit (1 ≤ n ≤ 2^{22}), q is an integer representing the number of queries (1 ≤ q ≤ 10^6), and encrypted_values is a list of q integers representing the encrypted values of v (0 ≤ e_i < n).
def func_1(n, q, encrypted_values):
    a = []
    last = 0
    results = []
    for i in range(q):
        v = (encrypted_values[i] + last) % n
        
        a.append(v)
        
        f_a = func_2(a)
        
        last = f_a
        
        results.append(f_a)
        
    #State of the program after the  for loop has been executed: `i` is `q - 1`; `q` must be greater than 0; `v` is `(encrypted_values[q-1] + last) % n`; `a` is a list of length `q` where each element is `v`; `f_a` is the return value of `func_2(a)`; `last` is `f_a`; `results` is a list of length `q` where each element is `f_a`.
    return results
    #`results` is a list of length `q` where each element is `f_a`
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, `q`, and `encrypted_values`. It processes `q` encrypted values using a rolling computation and a helper function `func_2`. Specifically, it iterates over each of the `q` encrypted values, computes the current value `v` as the sum of the current encrypted value and the last computed value modulo `n`, appends `v` to a list `a`, and then calls `func_2` with the updated list `a`. The result of `func_2` is stored in `last` and added to the `results` list. After completing the loop, the function returns the `results` list, which contains `q` elements, each being the output of `func_2` after processing each encrypted value. This process ensures that each element in `results` reflects the cumulative effect of the computations performed on the corresponding encrypted values.

#State of the program right berfore the function call: b is a list of non-negative integers, and the function calculates the difference between the maximum and minimum values in the list.
def func_2(b):
    max_val = max(b)
    min_val = min(b)
    return max_val - min_val
    #`The program returns the difference between the maximum value and the minimum value in list 'b'`
#Overall this is what the function does:The function `func_2` accepts a parameter `b`, which is a list of non-negative integers. It calculates and returns the difference between the maximum value and the minimum value in the list `b`. If the list is empty, the function will raise a `ValueError` because the `min()` and `max()` functions cannot operate on an empty list. If the list contains only one element, the function will return 0 since the difference between the single value and itself is zero.

