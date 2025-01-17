def remove_uppercase(s):
    # Using list comprehension to filter out uppercase characters
    result = ''.join([char for char in s if not char.isupper()])
    return result

# Test cases
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'
