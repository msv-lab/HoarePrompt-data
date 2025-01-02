#State of the program right berfore the function call: H is a positive integer (1 ≤ H ≤ 10^12), n is a positive integer (1 ≤ n ≤ 2⋅10^5), and d is a list of integers of length n (-10^6 ≤ d_i ≤ 10^6).
def func():
    h, n = map(int, raw_input().split())
    l = map(int, raw_input().split())
    mneg = 0
    som = 0
    neg = 0
    for i in xrange(n):
        if l[i] < 0:
            neg += l[i]
        else:
            if neg < mneg:
                mneg = neg
            neg = 0
        
        som += l[i]
        
    #State of the program after the  for loop has been executed: `h` is an input integer, `n` is an input integer, `d` is a list of integers of length `n` (-10^6 ≤ d_i ≤ 10^6), `l` is a map object of integers from the input, `som` is the sum of all elements in `l`, `mneg` is the minimum cumulative sum of consecutive negative numbers in `l`, `neg` is the cumulative sum of the last sequence of consecutive negative numbers in `l` or 0 if the last element is non-negative, `i` is `n - 1`.
    if (neg < mneg) :
        mneg = neg
    #State of the program after the if block has been executed: *`h` is an input integer, `n` is an input integer, `d` is a list of integers of length `n` (-10^6 ≤ d_i ≤ 10^6), `l` is a map object of integers from the input, `som` is the sum of all elements in `l`, `i` is `n - 1`. If `neg` < `mneg`, then `mneg` is updated to the current value of `neg`. `neg` remains the cumulative sum of the last sequence of consecutive negative numbers in `l` or 0 if the last element is non-negative.
    if (mneg * -1 > h) :
        li = h
        for i in xrange(n):
            li += l[i]
            
            if li <= 0:
                break
            
        #State of the program after the  for loop has been executed: `h` is an input integer, `n` is an input integer, `d` is a list of integers of length `n` (-10^6 ≤ d_i ≤ 10^6), `l` is a map object of integers from the input, `som` is the sum of all elements in `l`, `i` is the index at which the loop either breaks or completes (0 ≤ `i` < `n`), `neg` < `mneg`, `mneg` is the minimum value encountered during the loop, `neg` remains the cumulative sum of the last sequence of consecutive negative numbers in `l` or 0 if the last element is non-negative, `mneg * -1` is greater than `h`, `li` is `h + sum(l[:i+1])`. If `li` is less than or equal to 0, the loop breaks and `i` is the index where this condition is met. If the loop completes without breaking, `li` is the sum of all elements in `l` added to `h` and `i` is `n-1`.
        print(i + 1)
    else :
        if (som < 0) :
            li = h - (h / (som * -1) - 1) * (som * -1)
            for i in xrange(n):
                li += l[i]
                
                if li <= 0:
                    break
                
            #State of the program after the  for loop has been executed: `h` is an input integer, `n` is an input integer, `d` is a list of integers of length `n` (-10^6 ≤ d_i ≤ 10^6), `l` is a map object of integers from the input, `som` is the sum of all elements in `l`, `i` is the index at which `li` becomes less than or equal to 0 or `n-1` if the loop completes without breaking, `neg` is the cumulative sum of the last sequence of consecutive negative numbers in `l` or 0 if the last element is non-negative, `mneg` is updated to the current value of `neg` if `neg` < `mneg`, `mneg * -1` is less than or equal to `h`, `som` is less than 0, `li` is equal to `som * -1 + sum(l[:i+1])` if the loop breaks at index `i` or `som * -1 + sum(l)` if the loop completes without breaking.
            print((h / (som * -1) - 1) * n + i + 1)
        else :
            print('-1')
        #State of the program after the if-else block has been executed: *`h` is an input integer, `n` is an input integer, `d` is a list of integers of length `n` (-10^6 ≤ d_i ≤ 10^6), `l` is a map object of integers from the input, `som` is the sum of all elements in `l`, `i` is `n - 1`. If `neg` < `mneg`, then `mneg` is updated to the current value of `neg`. `neg` remains the cumulative sum of the last sequence of consecutive negative numbers in `l` or 0 if the last element is non-negative. Additionally, `mneg * -1` is less than or equal to `h`. If `som` is less than 0, `li` is equal to `som * -1 + sum(l[:i+1])` if the loop breaks at index `i` or `som * -1 + sum(l)` if the loop completes without breaking. If `som` is greater than or equal to 0, the state remains unchanged.
    #State of the program after the if-else block has been executed: *`h` is an input integer, `n` is an input integer, `d` is a list of integers of length `n` (-10^6 ≤ d_i ≤ 10^6), `l` is a map object of integers from the input, `som` is the sum of all elements in `l`, `i` is `n - 1`. If `neg` < `mneg`, then `mneg` is updated to the current value of `neg`. `neg` remains the cumulative sum of the last sequence of consecutive negative numbers in `l` or 0 if the last element is non-negative. If `mneg * -1` > `h`, then `li` is `h + sum(l[:i+1])`. If `li` is less than or equal to 0, the loop breaks and `i` is the index where this condition is met. If the loop completes without breaking, `li` is the sum of all elements in `l` added to `h` and `i` is `n-1`. The value of `i + 1` has been printed. If `mneg * -1` ≤ `h`, then if `som` < 0, `li` is equal to `som * -1 + sum(l[:i+1])` if the loop breaks at index `i` or `som * -1 + sum(l)` if the loop completes without breaking. If `som` ≥ 0, the state remains unchanged.
#Overall this is what the function does:The function processes two inputs: `H` (a positive integer representing an initial health value) and `n` (a positive integer representing the number of elements in a list of integers `d`). The function reads these inputs from standard input and then processes the list to determine the minimum number of steps required to reduce the health value (`H`) to zero or below. If the sum of all elements in the list is non-negative, the function prints `-1`, indicating that it's impossible to reduce the health value to zero or below. Otherwise, it calculates the number of steps required based on the cumulative sum of negative sequences and the total sum of the list, printing the result. The final state of the program includes the printed result and the processed variables, but the original inputs `H`, `n`, and `d` remain unchanged.

