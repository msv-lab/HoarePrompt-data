def func_1(string, substring):
    start = string.find(substring)
    if start == -1:
        return None
    end = start + len(substring)
    return (substring, start, end - 1)