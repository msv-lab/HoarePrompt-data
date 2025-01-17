def sum_even_and_even_index(lst):
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 == 0])
