#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n non-negative integers such that 0 ≤ a_i < n.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: Output State: The value of `t` will be exhausted after all inputs are processed, `n` will vary based on each input, `a` will remain unchanged as it is not modified within the loop, `b` will be updated such that each element in `b` corresponds to the count of its index in the input lists `s`, and `r` will contain concatenated strings resulting from the indices of elements in `s` according to the current state of `b`.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads an integer \( n \), followed by a list of \( n \) non-negative integers. It then maps these integers to characters from a predefined string `a` based on their index in a count array `b`. The function updates the count array `b` to reflect the occurrences of each integer in the input list and constructs a string `r` by concatenating the corresponding characters from `a`. Finally, it prints the constructed string `r` for each test case. After processing all test cases, the function outputs a series of strings, each derived from the input lists according to the described mapping.

