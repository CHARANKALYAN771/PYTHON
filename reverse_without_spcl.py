strSample='abc/defgh$ij'
 
#convert string into list
listSample=list(strSample)
 
i=0
j=len(listSample)-1
 
while i<j:
    if not listSample[i].isalpha():
        i+=1
    elif not listSample[j].isalpha():
        j-=1
    else:
        #swap the element in the list 
        #if both elements are alphabets
        listSample[i], listSample[j]=listSample[j], listSample[i]
        i+=1
        j-=1
print(listSample)
strOut=''.join(listSample)
print(strOut)