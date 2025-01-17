#State of the program right berfore the function call: x is a positive integer such that 1 ≤ x < 2^{30}.
def func_1(x):
    if (x == 1) :
        return [1]
        #The program returns [1]
    #State of the program after the if block has been executed: x is a positive integer such that 1 ≤ x < 2^{30}, and x is not equal to 1
    bits = []
    while x > 0:
        bit = x & 1
        
        bits.append(bit)
        
        x >>= 1
        
    #State of the program after the loop has been executed: `x` is 0, `bits` is a list containing the binary representation of the original value of `x` in reverse order.
    n = len(bits)
    a = [0] * n
    for i in range(n - 1):
        if bits[i]:
            a[i] = 1
        
        if bits[i + 1]:
            a[i + 1] = -1
        
    #State of the program after the  for loop has been executed: `x` is 0, `bits` is [0, True] if `n` is 1, otherwise `bits` is [0, True, True, ..., True] with `n-1` Trues, `a` is [1, -1, -1, ..., -1] with `n-2` -1s appended if `n` is greater than 1, otherwise `a` is [1, -1], and `n` must be a positive integer.
    return a
    #The program returns the list `a` which is [1, -1] if `n` is 1, otherwise it is [1, -1, -1, ..., -1] with `n-2` -1s appended
#Overall this is what the function does:The function `func_1` accepts a positive integer `x` such that \(1 \leq x < 2^{30}\). If `x` is 1, it returns the list `[1]`. Otherwise, it constructs a list `a` where the first element is `1`, followed by `-1` repeated `n-2` times, where `n` is the number of bits in the binary representation of `x` (excluding the last bit), and returns this list `a`.

