def longest_substring(s: str) -> int:
    
    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 
    pass
def longest_substring(s):
    if not s:
        return 0

    char_index = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        else:
            max_length = max(max_length, end - start + 1)
        char_index[s[end]] = end

    return max_length
