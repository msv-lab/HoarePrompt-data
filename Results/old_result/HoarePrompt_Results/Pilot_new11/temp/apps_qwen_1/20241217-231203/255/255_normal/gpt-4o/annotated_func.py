#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 500, `s` is a string input by the user with a length equal to `n`, and `operations` is the number of positions `i` (from 1 to `n-1`) where `s[i]` is not equal to `s[i-1]`.
    print(operations)
#Overall this is what the function does:The function reads an integer \( n \) and a string \( s \) of length \( n \) from the user. It then counts the number of positions \( i \) (from 1 to \( n-1 \)) where the character at position \( i \) in the string is different from the character at position \( i-1 \). Finally, it prints the total count of such positions. The function does not accept any parameters and does not return any value.

