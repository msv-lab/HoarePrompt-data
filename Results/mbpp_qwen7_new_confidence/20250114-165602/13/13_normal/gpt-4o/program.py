def remove_dirty_chars(first_str, second_str):
    # Create a set of characters from the second string for quick lookup
    dirty_set = set(second_str)
    
    # Use a list comprehension to filter out the characters
    result = ''.join([char for char in first_str if char not in dirty_set])
    
    return result

# Tests
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'
