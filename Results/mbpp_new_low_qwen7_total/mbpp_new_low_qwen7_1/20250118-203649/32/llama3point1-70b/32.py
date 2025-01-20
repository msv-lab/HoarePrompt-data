def is_samepatterns(patterns1, patterns2):
    if len(patterns1) != len(patterns2):
        return False
    
    mapping = {}
    for p1, p2 in zip(patterns1, patterns2):
        if p1 not in mapping:
            mapping[p1] = p2
        elif mapping[p1] != p2:
            return False
    
    return True
