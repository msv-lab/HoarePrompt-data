#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^18) and k is a positive integer (1 ≤ k ≤ 10^5).
def func_1(n, k):
    if (k > n) :
        return 'No'
        #The program returns 'No' because the current value of k is greater than n, where n is a positive integer (1 ≤ n ≤ 10^18) and k is a positive integer (1 ≤ k ≤ 10^5)
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18), `k` is a positive integer (1 ≤ k ≤ 10^5), and `k` is less than or equal to `n`.
    bits = []
    for i in range(60, -1, -1):
        if n >> i & 1:
            bits.append(i)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 10^18), `k` is a positive integer (1 ≤ k ≤ 10^5), `k` is less than or equal to `n`, `bits` contains all the indices of the set bits in `n` (ranging from 0 to 60). If no bits are set, `bits` is an empty list.
    if (len(bits) > k) :
        return 'No'
        #The program returns 'No', indicating that there are more indices of the set bits in 'n' than the value of 'k', despite 'k' being a positive integer and less than or equal to 'n', and the fact that the length of 'bits' is greater than 'k'
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 10^18), `k` is a positive integer (1 ≤ k ≤ 10^5), `k` is less than or equal to `n`, `bits` contains all the indices of the set bits in `n` (ranging from 0 to 60), and the length of `bits` is less than or equal to `k`. If no bits are set, `bits` is an empty list.
    while len(bits) < k:
        smallest = bits.pop()
        
        bits.append(smallest - 1)
        
        bits.append(smallest - 1)
        
    #State of the program after the loop has been executed: `len(bits)` is equal to `k`, `bits` contains set indices from the range of original `smallest - 1` values down to some minimum based on how many times the loop iterated, `smallest` has been decremented several times depending on how many times the loop executed, and `n` remains a positive integer (1 ≤ n ≤ 10^18). If `k` was initially greater than the length of `bits`, then the loop would have executed enough times to finalize `bits`'s length to exactly `k`.
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
    #The program returns 'Yes' followed by the sorted elements of 'bits' as a space-separated string
#Overall this is what the function does:The function accepts two parameters, `n` (a positive integer within the range 1 to 10^18) and `k` (a positive integer within the range 1 to 100,000). It returns 'No' if `k` is greater than `n` or if the number of indices of set bits in `n` exceeds `k`. If the number of indices of set bits in `n` is less than or equal to `k`, it modifies the list of bit indices by adding decremented values until the list length equals `k`. Finally, it returns 'Yes' followed by the sorted list of these bit indices as a space-separated string. The function effectively checks the relationship between `n` and `k`, the number of set bits in `n`, and adjusts the indices of these bits as per the condition applied.

