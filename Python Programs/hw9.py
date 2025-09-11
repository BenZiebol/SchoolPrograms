import random
#combine====================================
# Purpose: combine 2 dictionaries and returns a new dictionary with them combined
# Input Parameter(s):
# d1-1st dictionary
# d2-2nd dictionary
# Return Value(s): dictionary-class
#==========================================
def combine(d1,d2):
    dSum=d1
    for i in d2:
        if i in dSum:
            dSum[i]+=d2[i]
        else:
            dSum[i]=d2[i]
    return dSum

#first_words===================================
# Purpose: finds and counts what the 1st word is for each line
# Input Parameter(s): fname-the file name to be used
# Return Value(s): dictionary-class
#==========================================

def first_words(fname):
    fn=open(fname)
    contents=fn.readlines()
    new_dict={}
    for i in range(len(contents)):
        if contents[i].split()[0] in new_dict:
            new_dict[contents[i].split()[0]]+=1
        else:
            new_dict[contents[i].split()[0]]=1
    fn.close()
    return new_dict
#first_words===================================
# Purpose: finds what the words following each word is
# Input Parameter(s): fname-the file name to be used
# Return Value(s): dictionary-class
#==========================================
def next_words(fname):
    fn=open(fname)
    contents=fn.readlines()
    new_dict={}
    for i in range(len(contents)):
        words=contents[i].split()
        for j in range(len(words)-1):
            this_word=contents[i].split()[j]
            next_word=contents[i].split()[j+1]
            if this_word in new_dict:
                if next_word in new_dict[this_word]:
                    new_dict[this_word][next_word]+=1
                else:
                    new_dict[this_word][next_word]=1
            else:
                new_dict[this_word]={next_word:1}
    fn.close()
    return new_dict

#fanfic===================================
# Purpose: prints 10 'sentences' based on first words and next words
# Input Parameter(s): fname-the file name to be used
# Return Value(s): NONE
#==========================================
def fanfic(fname):
    nxt_words=next_words(fname)
    start_words=first_words(fname)
    list_start=[]
    list_nxt=[]
    for i in start_words:
        for j in range(start_words[i]):
            list_start.append(i)
    fn=open(fname)
    for i in range(10):
        current_word=random.choice(list_start)
        current_sentence=current_word
        stop_condition=True
        while stop_condition:
            for j in nxt_words[current_word]:
                list_nxt.append(j) 
            current_word=random.choice(list_nxt)
            if current_word=='.':
                stop_condition=False
            current_sentence+=' '+current_word
        print(current_sentence)
    fn.close()
