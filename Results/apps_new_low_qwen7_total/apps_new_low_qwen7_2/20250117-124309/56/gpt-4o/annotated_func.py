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
        
    #State of the program after the  for loop has been executed: Output State: `i` is -1, `n` is a non-negative integer such that \(1 \leq n \leq 10^{18}\), `k` is a positive integer such that \(1 \leq k \leq 10^5\) and \(k \leq n\), `bits` is a list containing all indices `i` from 60 down to the highest set bit of `n`. The loop continues to decrement `i` from 60 to 0, appending each index where the corresponding bit of `n` is set (i.e., `n >> i & 1` evaluates to 1). Once `i` reaches -1, the loop terminates because the condition `i in range(60, -1, -1)` no longer holds true.
    #
    #Since the loop runs from 60 down to 0, it will continue to append indices to `bits` as long as the corresponding bits in `n` are set to 1. After the loop completes, `i` will be -1, indicating that all possible bits have been checked. The value of `n` remains unchanged unless the problem statement specifies otherwise, but since no operations are performed on `n` other than reading its bits, `n` remains the same. The variable `k` is not affected by the loop and remains within its initial bounds.
    if (len(bits) > k) :
        return 'No'
        #The program returns 'No'
    #State of the program after the if block has been executed: `i` is -1, `n` is a non-negative integer such that \(1 \leq n \leq 10^{18}\), `k` is a positive integer such that \(1 \leq k \leq 10^5\) and \(k \leq n\), `bits` is a list containing all indices `i` from 60 down to the highest set bit of `n`, and the length of `bits` is less than or equal to `k`
    while len(bits) < k:
        smallest = bits.pop()
        
        bits.append(smallest - 1)
        
        bits.append(smallest - 1)
        
    #State of the program after the loop has been executed: i is -1, n is a non-negative integer such that 1 ≤ n ≤ 10^18, k is a positive integer such that 1 ≤ k ≤ 10^5, and k ≤ n, bits is a list containing exactly k elements where the first len(bits) - 2 elements are unique indices of set bits in n, and the last two elements are the same and equal to the previous second-to-last element in bits.
    bits.sort(reverse=True)
    return 'Yes\n' + ' '.join(map(str, bits))
    #'Yes\n' followed by a space-separated string of integers contained in the list 'bits'
#Overall this is what the function does:The function `func_1` accepts two parameters: `n` (a non-negative integer such that \(1 \leq n \leq 10^{18}\)) and `k` (a positive integer such that \(1 \leq k \leq 10^5\)). It checks if the number of set bits in the binary representation of `n` is less than or equal to `k`. If `k` is greater than `n`, it immediately returns 'No'. If the number of set bits is greater than `k`, it also returns 'No'. Otherwise, it modifies the list of set bits by appending duplicates of the smallest set bit until the list contains exactly `k` elements. Finally, it sorts the list in reverse order and returns 'Yes' followed by a space-separated string of these integers.

