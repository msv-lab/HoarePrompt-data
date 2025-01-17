def find_substring(list_of_strings, substring):
    for string in list_of_strings:
        if substring in string:
            return True
    return False

# Tests
assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
assert find_substring(["red", "black", "white", "green", "orange"], "abc") == False
assert find_substring(["red", "black", "white", "green", "orange"], "ange") == True
