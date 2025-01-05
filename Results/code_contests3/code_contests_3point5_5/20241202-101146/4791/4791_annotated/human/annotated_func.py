#State of the program right berfore the function call: N is an integer between 2 and 500 (inclusive).**
def func():
    n = input()
    while n:
        n -= 1
        
        for j in range(n):
            print(bin(j + 1)[::-1].find('1') + 1)
        
    #State of the program after the loop has been executed: N` is an integer between 0 and 498, `n` is 0, `j` is `n-1`, the output value is 1
#Overall this is what the function does:The function `func` reads an integer input `n`, decrements it in a loop until reaching 0, and then iterates over a range based on `n`. For each element in the range, it prints the position of the rightmost set bit in the binary representation of the element. The function does not return any value.

