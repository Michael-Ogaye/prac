
def longest_substring(s):
    start = 0
    max_len = 0
    char_dict = {}
    max_substring = ''

    for i in range(len(s)):
        if s[i] in char_dict and char_dict[s[i]] >= start:
            start = char_dict[s[i]] + 1
        else:
            if i - start + 1 > max_len:
                max_len = i - start + 1
                max_substring = s[start:i+1]

        char_dict[s[i]] = i

    return max_substring
l=longest_substring('aabcdabcdefafbcdeakkkkkkkkkakk')
print(l)
