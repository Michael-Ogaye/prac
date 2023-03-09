def longest_consec(strarr,U):
    longest=0
    new_array=[]
    cons_str=None
    for k in range(len(strarr)):
        cons_str=''.join(strarr[k:k+2])
        
        new_array.append((cons_str,len(cons_str)))
        if len(cons_str)>longest:
            longest=len(cons_str)
    for j in new_array:
        if j[1]==longest:
            return j[0]
        
res=longest_consec(['Liam','baci','youuoprtertyu','utyyop'],3)
print(res)
