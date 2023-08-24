def count_letters(s, t):
    s_counts = {}
    t_counts = {}
    for letter in s:
        s_counts[letter] = s_counts.get(letter, 0) + 1
    for letter in t:
        t_counts[letter] = t_counts.get(letter, 0) + 1
    
    yay_count = 0
    whoops_count = 0
    
    for letter, count in s_counts.items():
        if letter not in t_counts:
            whoops_count += count
        else:
            t_count = t_counts[letter]
            min_count = min(count, t_count)
            t_counts[letter] -= min_count
            yay_count += min_count
    
    for letter in s_counts:
        if letter.islower() and letter.upper() in t_counts:
            t_count = t_counts[letter.upper()]
            min_count = min(s_counts[letter], t_count)
            t_counts[letter.upper()] -= min_count
            whoops_count += min_count
            
        elif letter.isupper() and letter.lower() in t_counts:
            t_count = t_counts[letter.lower()]
            min_count = min(s_counts[letter], t_count)
            t_counts[letter.lower()] -= min_count
            whoops_count += min_count
    
    return yay_count, whoops_count

s = input()
t = input()

yay_count, whoops_count = count_letters(s, t)
print(yay_count, whoops_count)