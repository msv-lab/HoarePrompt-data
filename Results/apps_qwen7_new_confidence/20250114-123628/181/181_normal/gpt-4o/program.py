def decode_message(encoded_str, k):
    n = len(encoded_str)
    # To attempt to form the message of length k
    decoded = []
    
    # Count the number of mandatory characters
    mandatory_chars = sum(1 for i in range(n) if encoded_str[i].isalpha() and (i == n-1 or encoded_str[i+1] not in '*?'))
    
    # Count the number of optional characters
    optional_candy = sum(1 for i in range(n) if encoded_str[i] == '?')
    optional_snowflake = sum(1 for i in range(n) if encoded_str[i] == '*')
    
    # Check if it's possible to form a message of length k
    if k < mandatory_chars or k > mandatory_chars + optional_candy + optional_snowflake * (k - mandatory_chars):
        return "Impossible"
    
    current_length = mandatory_chars
    i = 0
    
    while i < n and len(decoded) < k:
        if encoded_str[i].isalpha():
            if i + 1 < n and encoded_str[i + 1] in '*?':
                if encoded_str[i + 1] == '?':
                    if current_length < k:
                        decoded.append(encoded_str[i])
                        current_length += 1
                    i += 2
                elif encoded_str[i + 1] == '*':
                    while current_length < k and len(decoded) < k:
                        decoded.append(encoded_str[i])
                        current_length += 1
                    i += 2
            else:
                decoded.append(encoded_str[i])
                current_length += 1
                i += 1
        else:
            i += 1
    
    if len(decoded) == k:
        return ''.join(decoded)
    else:
        return "Impossible"

# Read input
encoded_str = input()
k = int(input())

# Get the result
result = decode_message(encoded_str, k)

# Print the result
print(result)
