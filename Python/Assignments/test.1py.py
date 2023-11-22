def k_words(sentence,length_of_word):
    for i in sentence.split(" "):
        if len(i)>length_of_word:
            print(i)

#k_words("I am very shy",2)

def remove_ith_char(words,char_position):

    words = words[:char_position] + words[char_position+1:]
    print(words)

remove_ith_char("I am very shy",13)

    
