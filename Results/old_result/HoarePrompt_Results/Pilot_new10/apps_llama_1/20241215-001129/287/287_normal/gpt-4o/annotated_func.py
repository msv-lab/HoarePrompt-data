#State of the program right berfore the function call: num is a positive integer such that 1 <= num <= 10^9.
def func_1(num):
    count = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `num` is unchanged, `i` is the smallest integer greater than the square root of the original value of `num`, and `count` is the total number of factors of the original value of `num`.
    return count
    #The program returns the total number of factors of the original value of `num`
#Overall this is what the function does:The function accepts a positive integer `num` and returns the total number of factors of `num` by iterating through integers up to its square root, counting both each factor and its corresponding pair (if different), thus covering all cases including perfect squares and numbers with an odd or even number of factors.

