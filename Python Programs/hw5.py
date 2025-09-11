
#convert=====================================
# Purpose: converts notes up or down scale by given amount
# Input Parameter(s):
# notes: List of strings-represents the notes to be scaled
# up: int-represents how many steps up or down the scale should be shifted
# Return Value(s): List of strings-representing the notes that got scaled
#==========================================
def convert(notes, up):
    up=(up%12)
    scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    positions=[]
    for i in notes:
        positions.append(scale.index(i))
    for i in range(len(positions)):
        if positions[i]+up>11:
            positions[i]+=up-12
        elif positions[i]+up<0:
            positions[i]+=up+12
        else:
            positions[i]+=up
    for i in range(len(positions)):
        notes[i]=scale[positions[i]]
    return notes


#triple_sum=====================================
# Purpose: adds 3 numbers in a given list to add up to the target value
# Input Parameter(s):
# num_lst: a list of numbers to be added together
# target: the value that 3 numbers should add to
# Return Value(s): Int:the number of returned options for adding to the number
#==========================================

def triple_sum(num_lst, target):
    counter=0
    for low in range(0,len(num_lst)-2):
        j=low+1
        for med in range(j,len(num_lst)-1):
            k=med+1
            for high in range(k,len(num_lst)):
                if num_lst[low]+num_lst[med]+num_lst[high]==target:
                    print(str(num_lst[low]),'+',str(num_lst[med]),'+',str(num_lst[high]),'=',str(target))
                    counter+=1 
    return counter

#no_front_teeth=====================================
# Purpose: returns a new list where no 's' or 'z' are on the the even positions (if using indexing rules)
# Input Parameter(s):
# names_list: list of names to be sorted through
# Return Value(s): list of strings: in the correct order to avoid saying s or z
#==========================================

def no_front_teeth(names_list):
    bad_names=[]
    good_names=[]
    new_list=[]
    tracker=0
    for i in names_list:
        amount=0
        amount+=i.count('z')
        amount+=i.count('s')
        amount+=i.count('Z')
        amount+=i.count('S')
        if amount>0:
            bad_names.append(i)
            tracker+=1
        else:
            good_names.append(i)
    if tracker>len(names_list)/2:
        print('Mission impossible: too many unpronounceable names')
        return []
    tracker=0
    for i in range(len(bad_names)):
        new_list.append(good_names[i])
        new_list.append(bad_names[i])
        tracker+=1
    for i in range(tracker,len(good_names)):
        new_list.append(good_names[i])
    return new_list


        
