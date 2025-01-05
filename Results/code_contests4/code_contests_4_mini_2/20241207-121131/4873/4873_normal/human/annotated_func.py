#State of the program right berfore the function call: A, B, and C are strings of length N (1 ≤ N ≤ 100) consisting of lowercase English letters.
def func_1():
    n = int(raw_input().strip())
    a = [raw_input().strip() for i in xrange(3)]
    foo = 0
    for i in xrange(n):
        bucket = {}
        
        for s in a:
            bucket[s[i]] = True
        
        foo += len(bucket) - 1
        
    #State of the program after the  for loop has been executed: `A`, `B`, and `C` are strings of length `N`; `a` is a collection with at least `n` elements; `bucket` contains entries for each unique character at each index from 0 to `n-1` of the first `n` elements of `a`; `foo` is increased by the total count of unique characters across all indices from 0 to `n-1` minus `n`.
    print(foo)
#Overall this is what the function does:The function accepts no parameters and reads an integer `n` followed by three strings `A`, `B`, and `C`, each of length `N` (1 ≤ N ≤ 100). It counts the total number of unique characters across all three strings at each index from 0 to `n-1`, subtracting `n` from this total, and prints the result. The function does not handle cases where the input strings may not match the expected length of `n`, leading to potential index errors if `n` is greater than the actual length of the strings.

