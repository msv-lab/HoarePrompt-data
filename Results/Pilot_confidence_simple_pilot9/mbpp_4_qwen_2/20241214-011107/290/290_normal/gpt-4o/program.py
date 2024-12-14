def text_match_wordz_middle(s):
    # Check if 'z' is in the string and not at the start or end
    if 'z' in s[1:-1]:
        return True
    return False

# Test cases
assert text_match_wordz_middle("pythonzabc.") == True
assert text_match_wordz_middle("zxyabc.") == False
assert text_match_wordz_middle("  lang  .") == False
