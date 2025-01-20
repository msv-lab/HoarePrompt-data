#State of the program right berfore the function call: n is a non-negative integer such that 1 ≤ n ≤ 10^18, and k is a positive integer such that 1 ≤ k ≤ 10^5.
def func_1(n, k):
    if (k > n) :
        return 'No'
        #The program returns 'No'
    #State of the program after the if block has been executed: n is a non-negative integer such that 1 ≤ n ≤ 10^18, k is a positive integer such that 1 ≤ k ≤ 10^5, and k is less than or equal to n
    bits = []
    for i in range(60, -1, -1):
        if n >> i & 1:
            bits.append(i)
        
    #State of the program after the  for loop has been executed: `total` is 10, `i` is -1, `n` is a non-negative integer such that \(1 \leq n \leq 10^{18}\), `k` is a positive integer such that \(1 \leq k \leq 10^5\) and \(k \leq n\), `bits` is a list containing all indices `i` from 60 down to the highest bit set in `n` (inclusive).
    if (len(bits) > k) :
        return 'No'
        #The program returns 'No'
    #State of the program after the if block has been executed: `total` is 10, `i` is -1, `n` is a non-negative integer such that \(1 \leq n \leq 10^{18}\), `k` is a positive integer such that \(1 \leq k \leq 10^5\) and \(k \leq n\), `bits` is a list containing all indices `i` from 60 down to the highest bit set in `n` (inclusive). The length of `bits` is less than or equal to `k`.
    while len(bits) < k:
        smallest = bits.pop()
        
        bits.append(smallest - 1)
        
        bits.append(smallest - 1)
        
    #State of the program after the loop has been executed: - Since the loop continues until `len(bits) == k`, the final state of `bits` will be a list with exactly `k` elements, where each element is the result of decrementing the smallest element of the previous list twice.
    #   - `total` and `i` remain unchanged.
    #   - `n` remains unchanged.
    #   - `k` remains unchanged.
    #   - `bits` will have `k` elements, with the last two being the smallest element of the final list minus one, and the rest of the elements will be derived from the previous iterations.
    #
    #### Conclusion
    #
    #The final output state after the loop has executed all necessary iterations to reach `len(bits) == k` is:
    #
    #Output State:
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
    #'Yes\n' followed by the elements of list 'bits' joined into a single string separated by spaces
#Overall this is what the function does:The function `func_1` accepts two parameters: `n` (a non-negative integer such that \(1 \leq n \leq 10^{18}\)) and `k` (a positive integer such that \(1 \leq k \leq 10^5\)). It first checks if `k` is greater than `n`, in which case it returns 'No'. If not, it constructs a list `bits` containing the indices of the bits set in `n`. If the length of `bits` is greater than `k`, it returns 'No'. Otherwise, it manipulates the `bits` list by decrementing the smallest element twice for each iteration until its length equals `k`. Finally, it sorts the `bits` list in reverse order and returns 'Yes' followed by the elements of `bits` as a single string separated by spaces.

