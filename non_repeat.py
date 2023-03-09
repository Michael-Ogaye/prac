def first_non_repeating_letter(string):
    #your code here
    occurance={}
    val='' or None
    was_upper=False
    for l in string:
        if l.isupper():
            occurance[l.lower()]+=1 or 1
            was_upper=True
        occurance[l.lower()]+=1  or 1 
        
    for c in occurance:
        if occurance[c]==1:
            if was_upper:
                val=c.upper()
            else:
                val=c
    return val


def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""

def first_non_repeating_letter(string):
    return next((x for x in string if string.lower().count(x.lower())==1), '')