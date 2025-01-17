def remove_dirty_chars(main_string, dirty_chars):
    return ''.join(char for char in main_string if char not in dirty_chars)
