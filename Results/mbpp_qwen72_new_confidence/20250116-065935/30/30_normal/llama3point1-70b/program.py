def comb_sort(nums):
    def get_next_gap(gap):
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap

    n = len(nums)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False

        for i in range(0, n - gap):
            j = i + gap
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                swapped = True

    return nums
