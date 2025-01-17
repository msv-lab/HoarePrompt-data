def find_substring(lst, substring):
    return any(substring in string for string in lst)
