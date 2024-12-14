def func_1(s, char):
    first_occurrence = s.find(char)
    last_occurrence = s.rfind(char)
    if first_occurrence != -1 and last_occurrence != -1:
        if first_occurrence == last_occurrence:
            return s.replace(char, '', 1)
        else:
            return s[:first_occurrence] + s[first_occurrence + 1:last_occurrence] + s[last_occurrence + 1:]
    else:
        return s