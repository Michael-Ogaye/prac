def longest_substring(s):
    # Initialize variables
    max_len = 0
    start = 0
    char_dict = {}

    # Iterate over each character in the string
    for i, char in enumerate(s):
        # If the character has been seen before and its last occurrence is after the start of the current substring
        if char in char_dict and char_dict[char] >= start:
            # Update the start of the current substring to be after the last occurrence of the character
            start = char_dict[char] + 1
        # Update the last occurrence of the character to be the current index
        char_dict[char] = i
        # Update the maximum length of the substring
        max_len = max(max_len, i - start + 1)

    return max_len
