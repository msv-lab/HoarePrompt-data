def decode_string(b):
    """
    Decode the given string b by restoring the original string s.
 
    Args:
        b (str): The encoded string.
 
    Returns:
        str: The decoded string s.
    """
    # Create a dictionary to store the mapping between characters in the encoded string b and their corresponding indices in the alphabet
    char_map = {}
    for i, c in enumerate(sorted(set(b))):
        char_map[c] = chr(ord('a') + (len(b) - i - 1))
 
    # Initialize an empty string to store the decoded string s
    s = ""
 
    # Iterate through the encoded string b
    for c in b:
        # Find the index of the character in the alphabet and map it to its corresponding character in the decoded string s
        s += char_map[c]
 
    return s
 
# Read the number of test cases
num_test_cases = int(input())
 
for _ in range(num_test_cases):
    # Read the length of the string b
    num_chars = int(input())
 
    # Read the encoded string b
    b = input()
 
    # Decode the string b and print the result
    print(decode_string(b))