import heapq as hq
def expensive_items(data, n):
  return hq.nlargest(n, data, key=lambda x: x['price'])
