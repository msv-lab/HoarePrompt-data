#State of the program right berfore the function call: s is a string of length 1 to 100, inclusive, consisting of lowercase Latin letters.
def func():
    s = raw_input().strip()
    letters = list(map(chr, range(ord('a'), ord('z') + 1)))
    vowels = list('aeiou')
    const = list(set(letters) - set(vowels) - set(['n']))
    p = True
    for i in xrange(len(s)):
        if s[i] in const and (i + 1 == len(s) or s[i + 1] not in vowels):
            p = False
            break
        
    #State of the program after the  for loop has been executed: `s` is a string of lowercase Latin letters, `i` is the last index of `s` or the index where the loop condition was met, `letters` is a list containing ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], `vowels` is a list containing ['a', 'e', 'i', 'o', 'u'], `const` is a list containing ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']. If any character in `s` is a consonant followed by a non-vowel (or the end of the string), then `p` is False. If no such condition is met throughout the string, `p` remains True.
    print['NO', 'YES'][p]
#Overall this is what the function does:The function `func` reads a string `s` from the user input, which is expected to be a string of length 1 to 100, inclusive, consisting of lowercase Latin letters. It checks whether every consonant (excluding 'n') in the string `s` is followed by a vowel. If this condition is met for all characters in the string, the function prints "YES"; otherwise, it prints "NO". The function does not return any value. After the function concludes, the state of the program includes the input string `s`, a list of all lowercase letters `letters`, a list of vowels `vowels`, a list of consonants excluding 'n' `const`, and a boolean `p` indicating whether the condition was met. Edge cases include strings with only vowels, strings with only consonants, and strings of length 1. If the string contains a single consonant that is not 'n', the function will print "NO" because there is no following character to check.

