#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^18, and k is a positive integer such that 1 ≤ k ≤ 10^5.
def func_1(n, k):
    if (k > n) :
        return 'No'
        #The program returns 'No' because the current value of k is greater than n, where n is an integer such that 1 ≤ n ≤ 10^18 and k is a positive integer such that 1 ≤ k ≤ 10^5.
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ n ≤ 10^18, `k` is a positive integer such that 1 ≤ k ≤ 10^5, and `k` is less than or equal to `n`.
    bits = []
    for i in range(60, -1, -1):
        if n >> i & 1:
            bits.append(i)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 10^18, `k` is a positive integer such that 1 ≤ `k` ≤ 10^5 and `k` is less than or equal to `n`, and `bits` contains all the indices of the set bits in the binary representation of `n` (from 0 to 60).
    if (len(bits) > k) :
        return 'No'
        #The program returns 'No'
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 10^18, `k` is a positive integer such that 1 ≤ `k` ≤ 10^5 and `k` is less than or equal to `n`, and `bits` contains all the indices of the set bits in the binary representation of `n` (from 0 to 60). The length of `bits` is less than or equal to `k`.
    while len(bits) < k:
        smallest = bits.pop()
        
        bits.append(smallest - 1)
        
        bits.append(smallest - 1)
        
    #State of the program after the loop has been executed: `len(bits)` is equal to `k`, `n` is an integer such that 1 ≤ `n` ≤ 10^18, `k` is a positive integer such that 1 ≤ `k` ≤ 10^5 and `k` ≤ `n`, `bits` contains k elements all of which are derived from the original bits, with each element being a non-negative integer less than or equal to the smallest original index in `bits`.
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
    #The program returns 'Yes' followed by the elements of the list 'bits' joined by spaces, where 'bits' contains k elements sorted in descending order and is derived from the original bits
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 10^18) and a positive integer `k` (1 ≤ k ≤ 10^5). It returns 'No' if `k` is greater than `n` or if the number of set bits in the binary representation of `n` is greater than `k`. If there are fewer set bits than `k`, the function generates `k` bits by decrementing the smallest index of the set bits and returns 'Yes' followed by the `k` bits sorted in descending order. If the number of set bits is equal to `k`, it returns 'Yes' followed by those bits.

