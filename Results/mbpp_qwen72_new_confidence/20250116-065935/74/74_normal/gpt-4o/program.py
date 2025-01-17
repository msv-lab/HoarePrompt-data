from collections import Counter

def max_occurrences(lst):
    if not lst:
        return None
    frequency = Counter(lst)
    max_count = max(frequency.values())
    for item, count in frequency.items():
        if count == max_count:
            return item

# Provided test cases
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == 2
assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18]) == 8
assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10]) == 20
