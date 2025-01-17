def removezero_ip(ip: str) -> str:
    # Split the IP address into its components
    parts = ip.split('.')
    # Strip leading zeroes from each part
    parts = [str(int(part)) for part in parts]
    # Join the parts back together with dots
    return '.'.join(parts)

# Test cases
assert removezero_ip("216.08.094.196") == '216.8.94.196'
assert removezero_ip("12.01.024") == '12.1.24'
assert removezero_ip("216.08.094.0196") == '216.8.94.196'
