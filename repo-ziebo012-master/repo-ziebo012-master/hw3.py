#print_121=================================
# Purpose: Prints 'who needs loops' 121 times
# does so by calling the helper_1 2 times and printing the message itself once
# this brings the total number of times the message has been written to 121 times 5*2*2*3*2+1=121
# Input Parameter(s): none
# Return Value(s): NONE-outputs a lot of printed lines
#==========================================
def print_121():
    print('Who needs loops?')
    print_121_helper_1()
    print_121_helper_1()


#print_121_helper_1==========================
# Purpose:aids in Printing 'who needs loops' 121 times
# this one calls the helper_2 5 times so the message is printed 60 times
# Input Parameter(s): none
# Return Value(s): NONE-outputs a lot of printed lines
#==========================================
def print_121_helper_1():
    print_121_helper_2()
    print_121_helper_2()
    print_121_helper_2()
    print_121_helper_2()
    print_121_helper_2()


#print_121_helper_2==========================
# Purpose:aids in Printing 'who needs loops' 121 times
# this one calls the helper_3 2 times so the message is printed 12 times
# Input Parameter(s): none
# Return Value(s): NONE-outputs a lot of printed lines
#==========================================
def print_121_helper_2():
    print_121_helper_3()
    print_121_helper_3()


#print_121_helper_3==========================
# Purpose:aids in Printing 'who needs loops' 121 times
# this one calls the helper_4 2 times so the message is printed 6 times
# Input Parameter(s): none
# Return Value(s): NONE-outputs a lot of printed lines
#==========================================
def print_121_helper_3():
    print_121_helper_4()
    print_121_helper_4()


#print_121_helper_4==========================
# Purpose:aids in Printing 'who needs loops' 121 times
# this one prints the message 3 times
# Input Parameter(s): none
# Return Value(s): NONE-outputs a lot of printed lines
#==========================================
def print_121_helper_4():
    print('Who needs loops?')
    print('Who needs loops?')
    print('Who needs loops?')



#start of part B



#choice==========================
# Purpose:prints out various choices that the user can choose from
# Input Parameter(s):
# text-gives the story for the user
# optionA-the first option that the user can choose from
# optionB-the second option the user can choose from
# optionC-the third option the user can choose from
# Return Value(s): string-the response/choice that the user chose
#==========================================
def choice(text,optionA,optionB,optionC):
    print(text)
    print()
    print('A.',optionA)
    print('B.',optionB)
    print('C.',optionC)
    response=input('Choose A, B, or C:')
    if response not in ['A','B','C']:
        print('Invalid option, defaulting to A')
        response='A'
    print()
    return response


#Start of part C
#notes for self- 4 choices, 1st choice leads to bad end and 2 other choices
#2nd choice leads to good ending and 2 other choices, one of which was an option
#that could of been gotten to from choice 1. 3rd choice leads to 4th choice and a good
#and bad ending. 4th choice has 2 good endings and 1 bad ending


#adventure==========================
# Purpose:prints out various choices that the user can choose from and tells a story with different outcomes
# Input Parameter(s): NONE
# Return Value(s): Boolean-True=good ending False=Bad ending
#==========================================
def adventure():
    response=choice('Welcome to this grand world generator! what type of world would you like to create?!','OOOH!!! MAGIC!','sounds boring, I want a better adventure','I want a cool fantasy world!')
    if response=='A':
        response=choice('Ummm.... ok cool? but I kind of need more details then that','Go into a REALLY long boring monologue about the type of world you wanna play in','Technology and magic working in tandem','I do not care, I just want MAGIC! I am going to be a mighty and powerful wizard!!!')
    elif response=='B':
        print("Sorry, that wasn't really an option. I don't know how that got left in there. Whelp I'll just blow up now")
        return False
    if response=='A':
        print('you and this program have a grand old time playing around in the world that you have created')
        return True
    if response=='C':
        response=choice('ok, but I still want more info in order to better build the world for you',"MAGIC MAGIC MAGIC MAGIC!","ummm... ok fine, how about magic and.... just a bit of tech","oh, ok I want a world like the ancient times but with magic. kind of like a RPG game")
    if response=='A':
        print('The computer programs gets annoyed at you and blows up')
        return False
    if response=='C':
        print('The computer describes a brilliant world with magic and dragons where you have a grand adventure of becoming a mighty wizard')
        return True
    response=choice('ONE last question, how many others do you want to play with us?','what? oh it does not matter, maybe 4-5?','Oh.... I thought it was just going to be the two of use','WHAT! social things?! no thanks (you leave)')
    if response=='A':
        print('you and your friends have a grand time in this world that has been created')
        return True
    elif response=='B':
        print('you and the computer program has fun with magic tanks blowing stuff up')
        return True
    elif response=='C':
        print('The computer program has had enough of your attitude and blows up the computer')
        return False


