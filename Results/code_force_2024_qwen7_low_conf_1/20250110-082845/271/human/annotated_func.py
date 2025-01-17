#State of the program right berfore the function call: n is an integer such that 1 <= n <= 30.
def func_1(n):
    magic_words = []
    for _ in range(n):
        length = random.randint(1, 30 * n)
        
        word = ''.join(random.choice(['X', 'O']) for _ in range(length))
        
        magic_words.append(word)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 30, `magic_words` is a list containing exactly `n` elements, each element being a string of random characters 'X' or 'O' with length between 1 and 30 * n.
    return magic_words
    #`The program returns a list named 'magic_words' containing exactly n elements, each element being a string of random characters 'X' or 'O' with a length between 1 and 30 * n`
#Overall this is what the function does:The function `func_1` accepts an integer `n` such that 1 ≤ n ≤ 30. It generates a list named `magic_words` containing exactly `n` elements. Each element in the list is a string consisting of random characters 'X' or 'O', with the length of each string ranging from 1 to 30 * n. The function returns this list.

#State of the program right berfore the function call: s is a string consisting of characters X and O, and the length of s is at least 1 and at most 30*n, where n is the number of magic words created by the program.
def func_2(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
        
    #State of the program after the  for loop has been executed: `substrings` is a set containing all possible non-empty substrings of `s`, `i` is `len(s)`, `j` is `len(s) + 1`, `s` is a string consisting of characters 'X' and 'O', and the length of `s` is at least 1 and at most 30*n.
    return len(substrings)
    #The program returns the number of non-empty substrings of string `s`
#Overall this is what the function does:The function `func_2` accepts a string `s` consisting of characters 'X' and 'O', and returns the total number of unique non-empty substrings of `s`. It achieves this by iterating over all possible substrings of `s` using two nested loops, adding each substring to a set to ensure uniqueness, and then returning the size of this set. The function covers all substrings of `s`, including those that start and end at the same index, and handles edge cases where the input string could be empty (though the problem statement guarantees the length of `s` is at least 1).

#State of the program right berfore the function call: magic_words is a list of n distinct strings, where each string consists of characters 'X' and 'O', and has a length between 1 and 30*n inclusive. power is an integer representing the power of a student's spell, which is guaranteed to be the power of some concatenation of two strings from magic_words.
def func_3(magic_words, power):
    for i in range(len(magic_words)):
        for j in range(len(magic_words)):
            spell = magic_words[i] + magic_words[j]
            if func_2(spell) == power:
                return i + 1, j + 1
        
    #State of the program after the  for loop has been executed: `magic_words` is a list of `n` distinct strings, `power` is an integer representing the power of a student's spell, `i` is the index of the found spell's first part, `j` is the index of the found spell's second part, `spell` is the concatenation of `magic_words[i]` and `magic_words[j]`, and if no such pair exists, `i` is `n` and `j` is `n`.
    return -1, -1
    #`-1, -1`
#Overall this is what the function does:The function `func_3` accepts a list of strings `magic_words` and an integer `power`. It iterates through all possible pairs of strings in `magic_words`, concatenates them, and checks if the `power` of the resulting spell matches the given `power`. If a matching spell is found, it returns the 1-based indices of the two parts of the spell. If no match is found after checking all pairs, it returns `(-1, -1)`.

