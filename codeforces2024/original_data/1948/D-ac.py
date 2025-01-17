def find_max_mirror_length(s):
    # Initialize the maximum length of tandem repeat found
    max_len = 0
    
    # Iterate over possible half-lengths of tandem repeats, starting from the largest
    for sub_len in range(len(s) // 2, 0, -1):
        match_count = 0  # Counter for matching characters in the current window
        
        # Slide a window of size `sub_len` over the string
        for i in range(len(s) - sub_len):
            # Check if the current character and its counterpart in the second half match
            if s[i] == s[i + sub_len] or s[i] == '?' or s[i + sub_len] == '?':
                match_count += 1  # Increment match count if they match or can be made to match
                
                # If a full tandem repeat of this length is found
                if match_count == sub_len:
                    max_len = max(max_len, sub_len)  # Update the maximum length found
                    break  # No need to check further for this length
            else:
                match_count = 0  # Reset match count if a mismatch is found
    
    return max_len  # Return the maximum half-length found

def main():
    test_cases = int(input())  # Read the number of test cases
    for _ in range(test_cases):
        s = input()  # Read the string for the current test case
        ans = find_max_mirror_length(s)  # Find the maximum tandem repeat length
        print(ans * 2)  # Output the full length of the tandem repeat

if __name__ == "__main__":
    main()