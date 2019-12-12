def main():
    #retrieves files with user input
    wordfile = input("Enter the name of the censored words file: ")
    censorfile = input("Enter the name of the file you'd like to censor: ")
    
    words= open(wordfile, 'r')
    censored= open(censorfile, 'r')
    
    #reads file and splits list of words 
    badwords= words.read().split(" ")
    sentence= censored.read().split(" ")
    
    #loops through each file and finds the bad words that are in the sentence
    for i in badwords:
        for w in range(0, len(sentence)):
            if i==sentence[w]:
                sentence[w]='*' * len(i)
                
    words.close()
    censored.close()
    censored= open(censorfile, 'w+') 

    #rewrites and saves new sentence with words censored out  
    for i in sentence:
        censored.write(i)
        censored.write(" ")

    censored.close()

main()
    

    

