#State of the program right berfore the function call: n is a non-negative integer of up to 18 digits and k is a positive integer of up to 5 digits.
def func_1(n, k):
    if (k > n) :
        return 'No'
        #The program returns string 'No'
    #State of the program after the if block has been executed: n is a non-negative integer of up to 18 digits and k is a positive integer of up to 5 digits, and k is less than or equal to n
    bits = []
    for i in range(60, -1, -1):
        if n >> i & 1:
            bits.append(i)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer of up to 18 digits, `k` is a positive integer of up to 5 digits and is less than or equal to the original value of `n`, `i` is -1, and `bits` is a list of indices representing the positions of bits set to 1 in the binary representation of `n`.
    if (len(bits) > k) :
        return 'No'
        #The program returns string 'No'
    #State of the program after the if block has been executed: `n` is a non-negative integer of up to 18 digits, `k` is a positive integer of up to 5 digits and is less than or equal to the original value of `n`, `i` is -1, `bits` is a list of indices representing the positions of bits set to 1 in the binary representation of `n`, and the number of bits set to 1 in the binary representation of `n` is less than or equal to `k`
    while len(bits) < k:
        smallest = bits.pop()
        
        bits.append(smallest - 1)
        
        bits.append(smallest - 1)
        
    #State of the program after the loop has been executed: `n` is a non-negative integer of up to 18 digits, `k` is a positive integer of up to 5 digits, `i` is -1, and `bits` has a length of `k` with its elements determined by the loop's manipulation to meet the length requirement, but not necessarily reflecting the actual bit positions of `n`.
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
    #The program returns a string starting with 'Yes\n' followed by the string representations of the elements in `bits`, a list of length `k` (up to 5 digits) with elements in descending order, separated by spaces.
#Overall this is what the function does:The function checks whether it's possible to set exactly `k` bits to 1 in the binary representation of a non-negative integer `n` by potentially shifting bits to the right. It accepts two parameters, `n` and `k`, where `n` is a non-negative integer of up to 18 digits and `k` is a positive integer of up to 5 digits. The function returns 'No' if `k` is greater than `n` or if the number of bits set to 1 in `n` is greater than `k`. Otherwise, it tries to meet the requirement of having exactly `k` bits set to 1 by shifting the rightmost set bit to the right and duplicating it until `k` bits are set. If this process is successful, the function returns 'Yes' followed by a list of `k` numbers representing the bit positions in descending order. Note that the bit positions in the returned list may not reflect the actual bit positions in the original number `n` due to the manipulation performed by the function. The function handles potential edge cases, including when `n` is 0, when `k` is 1, and when `n` has fewer than `k` bits set to 1. However, it does not handle cases where the input values exceed the specified digit limits or where the inputs are not integers.

