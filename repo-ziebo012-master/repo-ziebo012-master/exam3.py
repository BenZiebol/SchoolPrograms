#Ben Ziebol's exam 3 solutions


#problem A
def count_big(num_lst):
    if len(num_lst)<=0:
        return 0
    elif num_lst[0]>99:
        return 1+count_big(num_lst[1:])
    else:
        return count_big(num_lst[1:])
def two_big(lst_lst):
    if len(lst_lst)<=0:
        return 0
    else:
        return count_big(lst_lst[0])+two_big(lst_lst[1:])
#problem B
#def to_indexes(string):


#problem C
class Lake:
    def __init__(self,name,area,depth):
        self.name=name
        self.area=area
        self.depth=depth
    def __str__(self):
        return str(self.name)+' - Area: '+str(self.area)+', Depth: ' + str(self.depth)
    def __lt__(self,other):
        return self.area<other.area

#problem D
class House:
    def __init__(self, beds, baths, haunted):
        self.beds = beds
        self.baths = baths
        self.haunted = haunted
    def remove_ghosts(self):
        self.haunted = False
    def estimate_price(self):
        value = self.beds*3000+self.baths*2000
        if self.haunted:
            return value//2
        else:
            return value

class Mansion(House):
    def __init__(self,beds,baths):
        House.__init__(self,beds,baths,True)
    def remove_ghosts(self):
        print('Too spooky, call an expert')
    def estimate_price(self):
        return House.estimate_price(self)*5

#problem E
class Painting:
    def __init__(self, artist, area):
        self.artist = artist
        self.area = area
    def too_bulky(self):
        return self.area > 1000
        
class Sculpture:
    def __init__(self, artist, weight):
        self.artist = artist
        self.weight = weight
    def too_bulky(self):
        return self.weight > 500
def display_artist(artist,art_list):
    display_list=[]
    for i in art_list:
        if not i.too_bulky() and i.artist==artist:
            display_list.append(i)
    return display_list
