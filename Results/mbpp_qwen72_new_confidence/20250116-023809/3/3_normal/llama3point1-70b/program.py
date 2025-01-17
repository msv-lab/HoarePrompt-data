import heapq as hq
def heap_queue_largest(nums: list, n: int) -> list:
  largest_nums = hq.nlargest(n, nums)
  return largest_nums
