def find_missing_letter(chars):
    converted=chars
    is_upper=False
    missing_index=None
    
    if chars[0].isupper():
        is_upper=True
        converted=[x.lower() for x in chars ]
    convert_no=[ord(j) for j in converted]
    print(convert_no)
    for k,j in enumerate(convert_no):
                if k==len(convert_no)-1:
                    missing_index=None
                    break
                
                else:
                    if (convert_no[k+1]-convert_no[k])>1:
                        missing_index=k
                        print(missing_index)
                    

                
            
            
    if missing_index is None:
        return None
    else:
        if is_upper:
            return chr([ord(c)for c in chars][missing_index+1])
        return chr(convert_no[missing_index+1])

