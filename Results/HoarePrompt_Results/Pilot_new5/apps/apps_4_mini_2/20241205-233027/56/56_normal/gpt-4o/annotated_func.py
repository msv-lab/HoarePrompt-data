#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^18, and k is a positive integer such that 1 ≤ k ≤ 10^5.
def func_1(n, k):
    if (k > n) :
        return 'No'
        #The program returns 'No' because the current value of k is greater than n, where n is a positive integer such that 1 ≤ n ≤ 10^18 and k is a positive integer such that 1 ≤ k ≤ 10^5.
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^18, and `k` is a positive integer such that 1 ≤ `k` ≤ 10^5. The value of `k` is less than or equal to `n`.
    bits = []
    for i in range(60, -1, -1):
        if n >> i & 1:
            bits.append(i)
        
    #State of the program after the  for loop has been executed: `bits` contains the list of indices of the set bits (1s) in the binary representation of `n` from 0 to 60, `n` is a positive integer such that 1 ≤ `n` ≤ 10^18, and `k` is a positive integer such that 1 ≤ `k` ≤ 10^5. If `n` has no set bits, `bits` remains an empty list.
    if (len(bits) > k) :
        return 'No'
        #The program returns 'No'
    #State of the program after the if block has been executed: *`bits` contains the list of indices of the set bits (1s) in the binary representation of `n` from 0 to 60, `n` is a positive integer such that 1 ≤ `n` ≤ 10^18, and `k` is a positive integer such that 1 ≤ `k` ≤ 10^5. The length of `bits` is less than or equal to `k`. If `n` has no set bits, `bits` remains an empty list.
    while len(bits) < k:
        smallest = bits.pop()
        
        bits.append(smallest - 1)
        
        bits.append(smallest - 1)
        
    #State of the program after the loop has been executed: `bits` contains the original indices of the set bits in `n`, with `smallest - 1` appended multiple times until the length of `bits` equals `k`, `smallest` is the last element of the original `bits`, `n` is a positive integer, `k` is a positive integer equal to or greater than the final length of `bits`, and `len(bits)` is equal to `k`.
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
    #The program returns 'Yes' followed by the joined string representation of the elements in 'bits', which is sorted in descending order, where 'bits' has a length equal to 'k'.
#Overall this is what the function does:The function accepts two integers `n` and `k`, returning 'No' if `k` exceeds `n` or if there are more set bits in `n` than `k`. If there are fewer set bits than `k`, it adjusts the bits to reach a length of `k`, and then returns 'Yes' followed by the indices in sorted order.

