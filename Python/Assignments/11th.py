'''input_string = input('Enter the string:')
word_length = int(input('Enter the word length'))

temp = input_string.split(" ")
words_greater_than_k_lenght = []
for i in temp:
    if len(i)>word_length:
        words_greater_than_k_lenght.append(i)

print(words_greater_than_k_lenght)'''

import re

def run(string):
 
    # Make own character set and pass 
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
     
    # Pass the string in search 
    # method of regex object.    
    if(regex.search(string) == None):
        print("String is accepted")
         
    else:
        print("String is not accepted.")
     
 
string = "GeeksForGeeks"
a = run(string)

input_string = input('Enter the string:')

dict1 = {}
value 
for i in input_string:
    dict[i] = 


     

        
        
