import string
 
alphabet = string.ascii_lowercase
 
for i in range(int(input())):
    n = int(input())
    word = ""
    if n > 52:
        word += alphabet[n - 53] + "zz"
    elif n > 27:
        word += "a" + alphabet[n - 28] + "z"
    elif n == 27:
        word = "aay"
    else:
        word += "aa" + alphabet[n - 3]
    print(word)