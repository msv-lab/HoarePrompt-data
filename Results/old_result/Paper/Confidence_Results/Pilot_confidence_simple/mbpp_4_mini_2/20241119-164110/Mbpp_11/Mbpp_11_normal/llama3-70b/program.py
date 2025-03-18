def remove_Occ(s, c):
    first_occ = s.find(c)
    last_occ = s.rfind(c)
    if first_occ != -1 and last_occ != -1:
        return s[:first_occ] + s[first_occ+1:last_occ] + s[last_occ+1:]
    else:
        return s
