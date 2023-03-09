def hfreq(word):
    cont={}
    freq=0
    letter=[]
    for l in word:
    
        if cont.get(l) is not None:
            cont[l]+=1

        else:
            cont[l]=1

        if cont[l]>freq:
            freq=cont[l]

    for k in cont.keys():
        if cont[k]==freq:
            letter.append(k)         
    return (letter,freq)  

print(hfreq('gtreddggewqawerttw445uy'))