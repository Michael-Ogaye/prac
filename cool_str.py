def cool(s):
    cool_str=[]
    
    # sbtrs=[''.join(list(s)[s.index(i):s.index(i)+4]) for i in list(s) if s.index(i)<len(s)-4]
    sbtrs = [s[i:i+4] for i in range(len(s)) if i <= len(s)-4]
    for string in sbtrs:
        is_cool=False
        for letter in string:
            if string.count(letter)==1:
                is_cool=True
            else:
                is_cool=False
        if is_cool:
            cool_str.append(string)


    print(sbtrs)

    return len(cool_str)


print(cool('ogaye'))