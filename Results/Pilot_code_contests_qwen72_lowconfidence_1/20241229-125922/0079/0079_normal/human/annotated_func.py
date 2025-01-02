#State of the program right berfore the function call: The function should take two parameters: an integer n (2 ≤ n ≤ 100) representing the length of the string, and a string s of length n consisting of capital Latin letters.
def func():
    n = input()
    s = raw_input()
    d = {}
    for i in range(1, n):
        gram = s[i - 1:i + 1]
        
        if d.get(gram) == None:
            d[gram] = 1
        else:
            d[gram] += 1
        
    #State of the program after the  for loop has been executed: `n` is an input value, `s` is an input string of length `n` consisting of capital Latin letters, `d` is a dictionary where each key is a bigram (a substring of length 2) from `s` and each value is the count of occurrences of that bigram in `s`. If `n` is less than 2, `d` remains an empty dictionary.
    a = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(a[0][0])
#Overall this is what the function does:The function reads an integer `n` and a string `s` from the user, where `n` is expected to be between 2 and 100, and `s` is a string of length `n` consisting of uppercase Latin letters. It then constructs a dictionary `d` where each key is a bigram (a substring of length 2) from `s`, and each value is the count of occurrences of that bigram in `s`. If `n` is less than 2, the function does not process the string and `d` remains an empty dictionary. The function sorts the dictionary `d` by the counts of bigrams in descending order and prints the most frequent bigram. If multiple bigrams have the same highest frequency, it prints the first one encountered in the sorted list. The function does not return any value.

