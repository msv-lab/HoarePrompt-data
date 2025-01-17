def sort_counter(counter_dict):
  return sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
