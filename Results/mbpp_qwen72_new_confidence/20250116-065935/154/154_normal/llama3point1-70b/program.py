def dict_depth(dictionary):
  if not isinstance(dictionary, dict) or not dictionary:
    return 0
  elif all(not isinstance(value, dict) for value in dictionary.values()):
    return 1
  else:
    return 1 + max(dict_depth(value) for value in dictionary.values() if isinstance(value, dict))
