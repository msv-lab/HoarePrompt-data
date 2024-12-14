#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 500; `s` is a string of length equal to `n`; `operations` is 1 plus the number of transitions between consecutive characters in `s`. If `n` is 1, `operations` remains 1.
    print(operations)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 500) and a string `s` of length `n` consisting of lowercase Latin letters. It counts and prints the number of segments in `s`, where a segment is defined as a continuous sequence of the same character interrupted by a different character. If `n` is 1, it returns 1 since there is only one segment.

