def count_reverse_pairs(string_list):
    count = 0
    seen = set()
    
    for s in string_list:
        reverse_s = s[::-1]
        if reverse_s in string_list and reverse_s not in seen and s not in seen:
            count += 1
            seen.add(s)
            seen.add(reverse_s)
    
    return count

# Tests
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]) == 2
assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1
assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2
