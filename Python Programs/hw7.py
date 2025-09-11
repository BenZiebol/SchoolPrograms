#encrypt=====================================
# Purpose: encrypts the given message
# Input Parameter(s):
# message: the message to be encrypted
# encoding: the vaconian cipher to be used for encoding
# Return Value(s): String-the encoded message
#==========================================
def encrypt(message, encoding):
    message=message.lower()
    cipher=[]
    coded_message=''
    message=message.lower()
    for i in range(0,len(encoding),5):
        cipher.append(encoding[i:i+5])
    for i in message:
        if i.isalpha():
            coded_message+=cipher[ord(i)-ord('a')]
    return coded_message


#decrypt=====================================
# Purpose: encrypts the given message
# Input Parameter(s):
# message: the message to be decrypted
# encoding: the vaconian cipher to be used for decoding
# Return Value(s): String-the decoded message
#==========================================
def decrypt(message,encoding):
    message=message.lower()
    encoding=encoding.lower()
    cipher=[]
    coded_message=''
    message=message.lower()
    for i in range(0,len(encoding),5):
        cipher.append(encoding[i:i+5])
    for i in range(0,len(message),5):
        x=cipher.index(message[i:i+5])
        coded_message+=chr(ord('a')+x)
    return coded_message


#longest_common=====================================
# Purpose: finds the longest common substring
# Input Parameter(s):
# first: the first string to be evaluated
# second: the second string to be evaluated
# Return Value(s): string-the lonest common string between the two
#==========================================
def longest_common(first,second):
    longest_word=''
    holder=''
    start=0
    for i in first:
        for j in range(start,len(second)):
            dupe=False
            if holder+second[j] in first:
                holder+=second[j]
                dupe=True
            if len(holder)>len(longest_word):
                longest_word=holder
            if not dupe:
                holder=''
        start+=1
        holder=''
    return longest_word
#=====================================
# Purpose: translates a phrase into piglatin
# Input Parameter(s):
# phrase-the phrase to be translated
# 
# Return Value(s): string-the phrase translated to piglatin
#==========================================
def igpay(phrase):
    word_list=phrase.split()
    new_list=[]
    for i in word_list:
        new_list.append(igpay_translate(i))
    return ' '.join(new_list)

#vowel_find=====================================
# Purpose: finds the first vowel position
# Input Parameter(s):
# word-the word that vowel needs to be found in
# 
# Return Value(s): int-the index position of the first vowel
#==========================================
def vowel_find(word):
    tracker=0
    vowels='aeiou'
    for i in word:
        if i in vowels:
            return tracker
        tracker+=1
    return len(word)

#igpay_translate_helper=====================================
# Purpose: helps to translate the word to piglatin
# Input Parameter(s):
# word-the string to be converted into piglatin
# position-the index position of the first vowel
# Return Value(s): string-the word converted to piglatin
#==========================================
def igpay_translate_helper(word,position):
    if position==0:
        new_word=word[position:len(word)]+word[0:position]+'way'
    else:
        new_word=word[position:len(word)]+word[0:position]+'ay'
    return new_word

#igpay_translate=====================================
# Purpose: translates given word to piglatin 
# Input Parameter(s):
# word-the string to be converted into pig latin
# 
# Return Value(s): string-the word converted
#==========================================
def igpay_translate(word):
    capital=False
    punctuation='.!,?'
    pun_check=False
    for i in word:
        if i.isupper():
            capital=True
            word=word.lower()
        if i in punctuation:
            pun_check=True
            punctuation=i
            word=word[0:-1]
    word=igpay_translate_helper(word,vowel_find(word))
    if capital:
        word=word[0].upper()+word[1:len(word)]
    if pun_check:
        word=word+punctuation
    return word
