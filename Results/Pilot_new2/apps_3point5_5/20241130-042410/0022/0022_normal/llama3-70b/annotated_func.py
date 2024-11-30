#State of the program right berfore the function call: s is a string of length between 1 and 1000, consisting of only English letters.**
def func():
    s = input()
    n = len(s)
    is_spalindrome = True
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            is_spalindrome = False
            break
        
    #State of the program after the  for loop has been executed: s is a string of length between 1 and 1000, consisting of only English letters; n is the length of string s, n is at least 2; is_spalindrome is True, i is n // 2 - 1. The characters at index i in s are equal to the characters at index n - i - 1 for all i in the range of n // 2. The loop has successfully checked for palindrome property in the string s.
    print('TAK' if is_spalindrome else 'NIE')
#Overall this is what the function does:The function `func` takes input from the user as a string `s` of length between 1 and 1000, consisting of only English letters. It then checks if the string is a palindrome by iterating through its characters. If the characters at the symmetric positions are equal for all characters up to the middle of the string, it prints 'TAK' indicating that the string is a palindrome; otherwise, it prints 'NIE'. The function does not explicitly return any value.

