
def longest_path_to_similiar_letter(s):
    #go through the string,then if the string is encountered again keep how many steps of i:
   highst_ind=0
   l_dict={l:0 for l in s}
   count=0
   for i,l in enumerate(list(s)):
        
        for k in range(i+1,len(s)):
            
           
        
            if list(s)[i]==list(s)[k]:
            
                
                highst_ind=k-i-1
                l_dict[l]=highst_ind
   print(l_dict)
   if max([num for num in l_dict.values()])==0:
       return -1
   return max([num for num in l_dict.values()])
print(longest_path_to_similiar_letter('michaeli'))


