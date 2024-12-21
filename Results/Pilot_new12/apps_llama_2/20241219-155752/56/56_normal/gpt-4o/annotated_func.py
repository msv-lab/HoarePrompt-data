#State of the program right berfore the function call: n is an integer and 1 <= n <= 10^18, k is an integer and 1 <= k <= 10^5.
def func_1(n, k):
    if (k > n) :
        return 'No'
        #The program returns the string 'No'
    #State of the program after the if block has been executed: n is an integer and 1 <= n <= 10^18, k is an integer and 1 <= k <= 10^5, and k is less than or equal to n
    bits = []
    for i in range(60, -1, -1):
        if n >> i & 1:
            bits.append(i)
        
    #State of the program after the  for loop has been executed: `n` is an integer and 1 <= original `n` <= 10^18, `k` is an integer and 1 <= `k` <= 10^5, `k` is less than or equal to original `n`, `bits` is a list of indices of the bits in original `n` that are 1, in the order they appear from most significant to least significant, `i` is -1 if the loop executed, otherwise `i` remains unchanged and `bits` is an empty list if `n` is 0.
    if (len(bits) > k) :
        return 'No'
        #The program returns the string 'No'
    #State of the program after the if block has been executed: `n` is an integer and 1 <= original `n` <= 10^18, `k` is an integer and 1 <= `k` <= 10^5, `k` is less than or equal to original `n`, `bits` is a list of indices of the bits in original `n` that are 1, in the order they appear from most significant to least significant, `i` is -1 if the loop executed, otherwise `i` remains unchanged and `bits` is an empty list if `n` is 0, and the length of `bits` is less than or equal to `k`
    while len(bits) < k:
        smallest = bits.pop()
        
        bits.append(smallest - 1)
        
        bits.append(smallest - 1)
        
    #State of the program after the loop has been executed: `bits` length is `k`, `i` is -1, `n` and `k` remain unchanged from their original values
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
    #The program returns a string that starts with 'Yes\n' followed by the string representations of all elements in the `bits` list, which is a sorted list in descending order with length `k`.
#Overall this is what the function does:The function accepts two parameters, `n` and `k`, where `n` is an integer and `1 <= n <= 10^18`, and `k` is an integer and `1 <= k <= 10^5`. It returns either the string 'No' if `k` is greater than `n` or if the number of bits set in `n` is greater than `k`. Otherwise, it returns a string that starts with 'Yes\n' followed by a sorted list of `k` elements, which represents the indices of bits in `n` modified to have exactly `k` bits set. The function modifies the bits of `n` by duplicating the smallest bit until `k` bits are reached, and then returns the sorted list of modified bit indices. The function handles edge cases where `n` is 0 or `k` is 1, and ensures that the returned list has exactly `k` elements.

