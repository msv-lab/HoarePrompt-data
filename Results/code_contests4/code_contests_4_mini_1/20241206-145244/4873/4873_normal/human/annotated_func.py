#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 100, and A, B, and C are strings of length N consisting of lowercase English letters.
def func_1():
    n = int(raw_input().strip())
    a = [raw_input().strip() for i in xrange(3)]
    foo = 0
    for i in xrange(n):
        bucket = {}
        
        for s in a:
            bucket[s[i]] = True
        
        foo += len(bucket) - 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 100; `n` is at least 1; `foo` is increased by `(n * (number of distinct elements in a - 1))`; `i` is equal to `len(a)`; `bucket` contains keys for all distinct elements in `a` for each iteration; `a` is a list with at least `len(a)` elements.
    print(foo)
#Overall this is what the function does:The function accepts three strings A, B, and C, each of length N (where 1 <= N <= 100). It calculates the number of distinct characters at each index across the three strings and sums the count of these distinct characters minus one for each index. Finally, it prints the total sum. The function does not explicitly return any value; it only prints the result.

