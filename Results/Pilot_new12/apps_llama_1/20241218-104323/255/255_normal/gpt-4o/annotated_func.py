#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `s` is an input string, `operations` is 1 plus the number of pairs of adjacent characters in `s` that are not equal, or 1 if `n` is 1 or less.
    print(operations)
#Overall this is what the function does:The function accepts an integer `n` and a string `s` of length `n` consisting of lowercase Latin letters from the user, counts the number of transitions between different characters in the string (i.e., the number of pairs of adjacent characters that are not equal) plus one, and prints this count as its output, effectively measuring the minimum number of distinct characters needed to represent the string by considering each transition as a new distinct character. The function does not handle cases where `n` is outside the range 1 to 500 or where `s` contains non-lowercase Latin letters, despite the annotations suggesting such constraints. After the function concludes, the program's state is that it has printed the count of operations (transitions plus one) to the console, without modifying the input string or integer.

