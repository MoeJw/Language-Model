from nltk import bigrams
import nltk
import math
import time
from collections import  defaultdict
from nltk.tokenize import RegexpTokenizer
import pickle
tokenizer = RegexpTokenizer(r'\w+')


def compute():
    
    for x in range(len(one)):  # to add the number of occurrences of word1 followed with word2
        if(one[x] in dic):
            dic[one[x]]+=1.0
        
        else:
            dic[one[x]]=1.0
    print words['at'],words['the']#dic[('at','the')]
    print words['it'],words['is']#dic[('it','is')]
    dic[("UNK","UNK")]=0
    for key in dic.iteritems():
        if(key in dic):
            #*
            dic[key]=((dic[key]+0.0+1)*words[key[0]])/(words[key[0]]+n)
#----------------------------------------------

def pre(string):

    tokens=tokenizer.tokenize(string) 
    porter=nltk.PorterStemmer()
    two=[porter.stem(x) for x in tokens ]
    two=list(bigrams(two))
    print two
 
    #sum=(words[two[0][0]]+0.0)/n
    sum=0
    UNK={}
    #sum=math.log(sum)
    
    for x in two:
        if x in dic:

           
            sum=sum+math.log(dic[x])
            #sum=sum*dic[x]
        else:   
                if(x[0] not in words and x[1] not in words ):
                    if(x[0] not in UNK and x[1] not in UNK):   
                        words[("UNK","UNK")]+=2

                    temp=(words[("UNK","UNK")]+0.0)/(words[("UNK","UNK")]+n)
                    dic[("UNK","UNK")]=temp
                    sum=sum+math.log(dic[("UNK","UNK")])
                    
                    pass
                elif(x[0] not in words and x[1]  in words):
                        if(x[0] not in UNK):
                                words[("UNK","UNK")]+=1
                        temp=(words[("UNK","UNK")]+0.0)/(words[("UNK","UNK")]+n)
                        dic[("UNK","UNK")]=temp
                        temp=(words[("UNK","UNK")]+0.0)/(words[("UNK","UNK")]+n)
                        sum=sum+math.log(temp)
            
                elif(x[0] in words and x[1]  not in words):
                     if(x[1] not in UNK):
                        words[("UNK","UNK")]+=1
                     temp=(words[x[0]]+0.0)/(words[x[0]]+n)
                     sum=sum+math.log(temp)
                     
                elif(x[0] in words and x[1] in words):
    
                    temp=(words[x[0]]+0.0)/(words[x[0]]+n)
                    sum=sum+math.log(temp)
                    #sum*=temp
                    
                   
           



    print sum
            
#----------------------------------------------


file=open("words.txt","r")
tokens=[]
words={}
start_time = time.time()
# your code
"""string=""
for line in file:
    string+=line
    

tokens=tokenizer.tokenize(string) 
porter=nltk.PorterStemmer()
tokens=[porter.stem(x) for x in tokens ]"""
data=file.readlines() 
for word in data:
     tokens.append(word[:-1])


print "after read tokens"

for x in xrange(len(tokens)):     # count the frequency of each word 
    if(tokens[x] in words):
        words[tokens[x]]+=1
    else:
       
        words[tokens[x]]=1


words[("UNK","UNK")]=0

print "after words"
#dic=defaultdict(lambda: defaultdict(lambda: 1)) #make the matrix 
dic={}
one=list(bigrams(tokens))
print "after bigram"

n=1812418
compute()


pre("  At the " )
pre(" it is ")
"""with open('dic', 'wb') as file:
 
  pickle.dump(dic, file)"""
elapsed_time = time.time() - start_time
print "time elapsed  ",elapsed_time





 