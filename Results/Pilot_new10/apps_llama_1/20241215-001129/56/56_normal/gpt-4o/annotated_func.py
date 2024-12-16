#State of the program right berfore the function call: n is a non-negative integer and k is a positive integer such that 1 ≤ k ≤ 10^5 and 1 ≤ n ≤ 10^18.
def func_1(n, k):
    if (k > n) :
        return 'No'
        #The program returns string 'No'
    #State of the program after the if block has been executed: n is a non-negative integer and k is a positive integer such that 1 ≤ k ≤ 10^5 and 1 ≤ n ≤ 10^18, and k is less than or equal to n
    bits = []
    for i in range(60, -1, -1):
        if n >> i & 1:
            bits.append(i)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `k` is a positive integer such that 1 ≤ k ≤ 10^5 and 1 ≤ n ≤ 10^18, and k is less than or equal to n, `bits` is a list containing the indices of all bits in the original value of `n` that are 1, in descending order, and `i` is -1.
    if (len(bits) > k) :
        return 'No'
        #The program returns the string 'No'
    #State of the program after the if block has been executed: `n` is a non-negative integer, `k` is a positive integer such that 1 ≤ k ≤ 10^5 and 1 ≤ n ≤ 10^18, and k is less than or equal to n, `bits` is a list containing the indices of all bits in the original value of `n` that are 1, in descending order, `i` is -1, and the number of bits set in `n` (i.e., the length of `bits`) is less than or equal to `k`
    while len(bits) < k:
        smallest = bits.pop()
        
        bits.append(smallest - 1)
        
        bits.append(smallest - 1)
        
    #State of the program after the loop has been executed: `bits` contains `k` elements, with the original bits and additional bits set to `smallest - 1` where `smallest` is the smallest original index in `bits`, `i` is -1, and `n` and `k` retain their original values.
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
    #The program returns a string 'Yes' followed by k elements of 'bits' that are sorted in descending order, where 'bits' contains original bits and additional bits set to 'smallest - 1'.
#Overall this is what the function does:The function accepts a non-negative integer `n` and a positive integer `k`, and returns 'Yes' followed by `k` sorted bit indices in descending order if it's possible to have `k` bits set in the binary representation of `n` by potentially adding new bits, and 'No' otherwise

