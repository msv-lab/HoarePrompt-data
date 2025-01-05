#State of the program right berfore the function call: N is a positive integer. A, B, and C are strings of length N consisting of lowercase English letters.**
def func_1():
    n = int(raw_input().strip())
    a = [raw_input().strip() for i in xrange(3)]
    foo = 0
    for i in xrange(n):
        bucket = {}
        
        for s in a:
            bucket[s[i]] = True
        
        foo += len(bucket) - 1
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, `foo` will be equal to the sum of unique characters in all strings A, B, and C minus 3 times the number of strings. `bucket` will contain all unique characters from the strings A, B, and C with values set to True.
    print(foo)
#Overall this is what the function does:The function `func_1` reads an integer N followed by three strings A, B, and C of length N each. It then counts the total number of unique characters across all three strings and subtracts 3 times the number of strings. The result is stored in the variable `foo`, which is printed at the end. The function does not explicitly return a value.

