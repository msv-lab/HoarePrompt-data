import re
def text_match_wordz(s):
  return bool(re.search(r'\bz\b', s))
