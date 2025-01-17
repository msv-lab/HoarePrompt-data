You have a dictionary, which is a list of distinct words sorted in
alphabetical order. Each word consists of uppercase English letters.

You want to print this dictionary. However, there is a bug with the printing
system, and all words in the list are printed next to each other without any
separators between words. Now, you ended up with a string S that is a
concatenation of all the words in the dictionary in the listed order.

Your task is to reconstruct the dictionary by splitting S into one or more
words. Note that the reconstructed dictionary must consist of distinct words
sorted in alphabetical order. Furthermore, you want to maximize the number of
words in the dictionary. If there are several possible dictionaries with the
maximum number of words, you can choose any of them.

Input

A single line consisting of a string S (1 \leq |S| \leq 5000) . String S
consists of only uppercase English letters.

Output

First, output an integer in a single line representing the maximum number of
the words in the reconstructed dictionary. Denote this number as n .

Then, output n lines, each containing a single string representing the word.
The words must be distinct, and the list must be sorted alphabetically. The
concatenation of the words in the listed order must equal S .

If there are several possible dictionaries with the maximum number of words,
output any of them.

Examples

Input

    ABACUS
    
Output

    4
    A
    BA
    C
    US

Input

    AAAAAA
    
Output

    3
    A
    AA
    AAA

Input

    EDCBA
    
Output

    1
    EDCBA
