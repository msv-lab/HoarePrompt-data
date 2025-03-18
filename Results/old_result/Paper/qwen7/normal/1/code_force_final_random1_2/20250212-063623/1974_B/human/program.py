def symmetric_encode(s):
    # Create a list of unique characters from the input string
    unique_chars = sorted(list({char for char in s}))
    
    i, j = 0, len(unique_chars) - 1
    
    # Encode the input string
    for char in s:
        if char in unique_chars:
            # Replace the current character with its symmetric counterpart
            s = s.replace(char, unique_chars[j])
            j -= 1
        else:
            # Add the new character to the unique_chars list
            unique_chars.insert(i, char)
            
            # Update i and j
            i += 1
            j += 1
    
    return ''.join(unique_chars)
 
# Main function
if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        b = input()
        
        # Get the encoded string
        encoded_str = symmetric_encode(b)
        
        # Print the encoded string
        print(encoded_str)