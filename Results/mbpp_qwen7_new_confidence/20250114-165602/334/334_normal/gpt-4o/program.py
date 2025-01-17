def remove_length(s: str, k: int) -> str:
    # Split the string into words
    words = s.split()
    
    # Filter out words of length k
    filtered_words = [word for word in words if len(word) != k]
    
    # Join the filtered words back into a string
    result = ' '.join(filtered_words)
    
    return result

# Tests
assert remove_length('The person is most value tet', 3) == 'person is most value'
assert remove_length('If you told me about this ok', 4) == 'If you me about ok'
assert remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'
