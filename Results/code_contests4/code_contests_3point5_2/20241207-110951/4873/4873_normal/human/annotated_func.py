#State of the program right berfore the function call: **
def func_1():
    n = int(raw_input().strip())
    a = [raw_input().strip() for i in xrange(3)]
    foo = 0
    for i in xrange(n):
        bucket = {}
        
        for s in a:
            bucket[s[i]] = True
        
        foo += len(bucket) - 1
        
    #State of the program after the  for loop has been executed: `n` is an integer value greater than or equal to 3, `a` is a list containing 3 or more strings, `foo` is the total number of unique characters at the respective positions in the strings minus 3, `i` is n, `bucket` is a dictionary with keys as characters at index n-1 of each string in `a` set to True
    print(foo)
#Overall this is what the function does:The function `func_1` reads an integer `n` and 3 strings into a list `a`. It then iterates `n` times, creating a dictionary `bucket` with keys as characters at the respective positions in the strings. The function calculates the total number of unique characters at each position in the strings and subtracts 3. Finally, it prints the resulting value `foo`. The function does not accept any parameters and does not have a specific return value.

