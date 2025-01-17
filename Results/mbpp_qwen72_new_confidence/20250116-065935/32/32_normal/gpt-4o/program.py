def is_samepatterns(lst1, lst2):
    if len(lst1) != len(lst2):
        return False

    map1 = {}
    map2 = {}

    for i in range(len(lst1)):
        if lst1[i] not in map1:
            map1[lst1[i]] = lst2[i]
        if lst2[i] not in map2:
            map2[lst2[i]] = lst1[i]
        if map1[lst1[i]] != lst2[i] or map2[lst2[i]] != lst1[i]:
            return False

    return True

# Test cases
assert is_samepatterns(["red","green","green"], ["a", "b", "b"]) == True
assert is_samepatterns(["red","green","greenn"], ["a","b","b"]) == False
assert is_samepatterns(["red","green","greenn"], ["a","b"]) == False
