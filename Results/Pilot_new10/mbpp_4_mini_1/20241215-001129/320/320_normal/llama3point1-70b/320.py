def second_smallest(nums):
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None
    return sorted(unique_nums)[1]
