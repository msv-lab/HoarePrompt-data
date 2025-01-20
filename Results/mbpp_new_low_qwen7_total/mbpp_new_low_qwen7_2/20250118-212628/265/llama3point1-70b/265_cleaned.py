def func_1(s, pattern):
    match = re.search(pattern, s)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return None