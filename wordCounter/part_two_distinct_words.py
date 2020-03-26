#description: Program counts number of distinct words in David Copperfield Novel
#author: Aziz, Muhammad
#date: 12.4.2018

#Function Defintions

def read_word_list():
     davidC = open('ENGLISH_LIT.txt')
     print ("OPEN")
     s=davidC.read()
     print ("DONE")
     return s.split()



def build_dictionary(word_list):
    davidDict={}
    for word in word_list:
         if word not in davidDict:
             davidDict[word]=1
         else:
             davidDict[word]+=1
    print("DICTIONARY CREATED")
    return davidDict 


def tuple_list(davidDict, frequency):
     tuple_list = []
     for word in davidDict:
          if davidDict[word] > frequency:
               tuple_list.append((davidDict[word] , word))
               tuple_list.sort(reverse=True)
     print(tuple_list)
               
     

#Main

word_list = read_word_list()
davidDict = build_dictionary(word_list)

n = int(input("Enter Freq: "))

print("TUPLE LIST")
tuple_list(davidDict, n)

