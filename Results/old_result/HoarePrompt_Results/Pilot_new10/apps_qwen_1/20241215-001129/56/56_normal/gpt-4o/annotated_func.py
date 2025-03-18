#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^18, and k is a positive integer such that 1 ≤ k ≤ 10^5.
def func_1(n, k):
    if (k > n) :
        return 'No'
        #The program returns 'No'
    #State of the program after the if block has been executed: `n` is a positive integer such that 1 ≤ n ≤ 10^18, `k` is a positive integer such that 1 ≤ k ≤ 10^5, and `k` is less than or equal to `n`
    bits = []
    for i in range(60, -1, -1):
        if n >> i & 1:
            bits.append(i)
        
    #State of the program after the  for loop has been executed: `n` is an integer, `k` is a positive integer, and `bits` is a list containing the indices of the bits set to 1 in `n`.
    if (len(bits) > k) :
        return 'No'
        #The program returns 'No'
    #State of the program after the if block has been executed: `n` is an integer, `k` is a positive integer, `bits` is a list containing the indices of the bits set to 1 in `n`, and the length of `bits` is less than or equal to `k`.
    while len(bits) < k:
        smallest = bits.pop()
        
        bits.append(smallest - 1)
        
        bits.append(smallest - 1)
        
    #State of the program after the loop has been executed: `n` is an integer, `k` is a positive integer, `bits` is a list of length `k` containing the indices of the bits set to 1 in `n` where each index is either the original index or one less than the original index of the smallest bit index popped from `bits`.
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
    #'Yes\n' followed by a space-separated string of the elements in the list 'bits', which is sorted in reverse order and contains the indices of the bits set to 1 in 'n' where each index is either the original index or one less than the original index of the smallest bit index popped from 'bits'
#Overall this is what the function does:The function `func_1` accepts two parameters `n` and `k`, where `n` is a positive integer such that \(1 \leq n \leq 10^{18}\) and `k` is a positive integer such that \(1 \leq k \leq 10^5\). The function returns 'No' if `k` is greater than `n` or if the number of bits set to 1 in the binary representation of `n` is greater than `k`. Otherwise, it processes the list of bit indices, adjusts them as needed, sorts the list in reverse order, and returns 'Yes' followed by a space-separated string of the modified bit indices.

