while True:
    char = input("Enter a character: ")
    if(char=='A' or char=='a' or char=='E' or char =='e' or char=='I' or char=='i' or char=='O' or char=='o' or char=='U' or char=='u'):
       print(char, "is a Vowel")
    elif(char=="$" or char=="&" or char=="#" or char=="@" or char=="^" or char=="{" or char== "}" or char=="," or char=="!" or char=="[" or char=="]" or char=="(" or char==")"):
        print(char,"is a special chracter")
    elif(char >= '0' and char <= '9'):
        print(char,"is a number")
    else:
        print(char, "is a Consonant")
