#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^18, and k is a positive integer such that 1 ≤ k ≤ 10^5.
def func_1(n, k):
    if (k > n) :
        return 'No'
        #The program returns 'No' because the current value of k is greater than n.
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ n ≤ 10^18, `k` is a positive integer such that 1 ≤ k ≤ 10^5, and `k` is less than or equal to `n`.
    bits = []
    for i in range(60, -1, -1):
        if n >> i & 1:
            bits.append(i)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 10^18, `k` is a positive integer such that 1 ≤ `k` ≤ 10^5, `k` is less than or equal to `n`, and `bits` is a list of indices of the set bits in the binary representation of `n`, ranging from 0 to 60.
    if (len(bits) > k) :
        return 'No'
        #The program returns 'No'
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 10^18, `k` is a positive integer such that 1 ≤ `k` ≤ 10^5, `k` is less than or equal to `n`, and `bits` is a list of indices of the set bits in the binary representation of `n`, ranging from 0 to 60. The length of `bits` is less than or equal to `k`.
    while len(bits) < k:
        smallest = bits.pop()
        
        bits.append(smallest - 1)
        
        bits.append(smallest - 1)
        
    #State of the program after the loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 10^18; `k` is a positive integer such that 1 ≤ `k` ≤ 10^5; `k` is less than or equal to `n`; `len(bits)` is equal to `k`; `smallest` is the value of the last element removed from `bits` during the final execution; `bits` now contains the indices of set bits in `n` with additional elements that are decremented values of the smallest elements that have been processed, ensuring that `len(bits)` has reached `k`.
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
    #The program returns 'Yes' followed by the indices of set bits in n, which are contained in the sorted list 'bits', formatted as a space-separated string.
#Overall this is what the function does:The function accepts two parameters, `n` (a positive integer between 1 and 10^18) and `k` (a positive integer between 1 and 10^5). It first checks if `k` is greater than `n`, in which case it returns 'No'. It then counts the number of set bits in the binary representation of `n` and if the count exceeds `k`, it again returns 'No'. If the count is less than or equal to `k`, it ensures that the total number of bits matches `k` by adding decremented indices of the smallest set bit until the count reaches `k`. Finally, it returns 'Yes' followed by the sorted indices of the set bits in `n` as a space-separated string. This function assumes `k` will not exceed the maximum possible number of bits (which is 60 in this context).

