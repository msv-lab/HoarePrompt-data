import heapq as hq

def larg_nnum(nums: list, n: int) -> list:
    return hq.nlargest(n, nums)
