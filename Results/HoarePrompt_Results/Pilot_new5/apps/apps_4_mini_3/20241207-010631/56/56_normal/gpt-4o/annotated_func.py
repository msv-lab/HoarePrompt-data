#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^18) and k is a positive integer (1 ≤ k ≤ 10^5).
def func_1(n, k):
    if (k > n) :
        return 'No'
        #The program returns 'No' because the current value of k is greater than n, where n is a positive integer (1 ≤ n ≤ 10^18)
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18), `k` is a positive integer (1 ≤ k ≤ 10^5), and `k` is less than or equal to `n`.
    bits = []
    for i in range(60, -1, -1):
        if n >> i & 1:
            bits.append(i)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 10^18), `k` is a positive integer (1 ≤ k ≤ 10^5), `k` is less than or equal to `n`, and `bits` contains the indices of all the bits that are set to 1 in the binary representation of `n`.
    if (len(bits) > k) :
        return 'No'
        #The program returns 'No' indicating that there are more indices of bits set to 1 in the binary representation of `n` than the value of `k`, where `k` is less than or equal to `n`.
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18), `k` is a positive integer (1 ≤ k ≤ 10^5), `k` is less than or equal to `n`, and `bits` contains the indices of all the bits that are set to 1 in the binary representation of `n`. The length of `bits` is less than or equal to `k`.
    while len(bits) < k:
        smallest = bits.pop()
        
        bits.append(smallest - 1)
        
        bits.append(smallest - 1)
        
    #State of the program after the loop has been executed: `bits` contains `k` elements, where each element is a non-negative integer. If `k` was initially greater than the original length of `bits`, the loop would not execute, and `bits` would remain unchanged. If `k` was less than or equal to the original length of `bits`, then `smallest` will be the smallest index from the original `bits` during the final iterations.
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
    #The program returns 'Yes' followed by the elements of the list 'bits' joined into a string, where 'bits' is sorted in reverse order (descending) and has 'k' elements retained.
#Overall this is what the function does:The function accepts two positive integers, `n` and `k`. It first checks if `k` is greater than `n`, returning 'No' if true. It then counts the number of bits set to 1 in the binary representation of `n`. If there are more bits set to 1 than `k`, it returns 'No'. If there are fewer or equal bits, it expands the list of bits to exactly `k` by duplicating the smallest bit until the size of the list equals `k`. Finally, the function returns 'Yes' followed by the `k` bit indices sorted in descending order. The function does not handle cases where `n` is zero, which may introduce unexpected behavior.

