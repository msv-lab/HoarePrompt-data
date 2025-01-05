#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 100, A, B, and C are strings of length N consisting of lowercase English letters.
def func_1():
    n = int(raw_input().strip())
    a = [raw_input().strip() for i in xrange(3)]
    foo = 0
    for i in xrange(n):
        bucket = {}
        
        for s in a:
            bucket[s[i]] = True
        
        foo += len(bucket) - 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 100; `i` is equal to `N`; `bucket` contains keys for every unique character found in the strings of `a` at indices 0 to `N-1`, with all values set to `True`; `foo` is the total count of unique characters across all strings in `a` minus the number of strings in `a`.
    print(foo)
#Overall this is what the function does:The function accepts three strings A, B, and C, each of length N, where N is a positive integer between 1 and 100. It computes and prints the total count of unique characters across all three strings at each character index, subtracting the number of strings (which is always 3) from this count. This means that if there are no unique characters at a specific index, it will not contribute to the total. The function will handle cases where all characters at a specific index are the same, resulting in no unique characters being counted.

