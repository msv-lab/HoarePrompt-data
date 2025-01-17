import re
def text_match_two_three(s):
  return bool(re.search('ab{2,3}', s))