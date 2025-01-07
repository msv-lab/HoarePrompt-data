#State of the program right berfore the function call: char is a string of length 1, i.e., a single character.
def func_1(char):
    """
    Returns the ASCII value of a given character.

    Parameters:
    char (str): A single character.

    Returns:
    int: The ASCII value of the character.
    """
    return ord(char)
    #The program returns the Unicode point for the single character string 'char'
#Overall this is what the function does:The function accepts a string and returns the Unicode point for the first character of the string, raising a TypeError if the string is empty

