def text_match_wordz_middle(s):
    words = s.split()
    for word in words:
        if len(word) > 1 and 'z' in word[1:-1]:
            return True
    return False
