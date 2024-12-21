def flatten_list(nested_list):
  flat_list = []
  for i in nested_list:
    if type(i) == list:
      flat_list.extend(flatten_list(i))
    else:
      flat_list.append(i)
  return flat_list
