# return masked string with all characters masked except for the last N characters
def maskify(cc, n: int = 4):
    num_chars = len(cc) - n  # the number of chars to mask
    return "#"*num_chars + cc[num_chars:] if num_chars > 0 else cc
