    word=input(("Input the word you want the secret code for: "))
    letters=list(word)
    lenght=(len(word))-1
    i=0
    value=[ord(char) for char in letters]
    while i<= lenght:
        if 0<= value[i]<65 or 91<=value[i]<=96 or 123<= value[i]<=127:
            value[i]=value[i]
        elif 65<= value[i]<= 85 or 97<= value[i] <= 117:
            value[i]=value[i]+5
        else:
            value[i]= value[i]-21
        i=i+1
    new_letter=[chr(num) for num in value]
    new_word=''.join(new_letter)
    print("The secret code is: " + new_word)
