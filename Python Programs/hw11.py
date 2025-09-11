#Complex===================================
# Purpose: Performs various methods (addition subtraction etc) on complex numbers
# Instance variables:
# real-represents the real component of complex number
# imag-represents the imaginary component of complex number
# Methods:
# __init__:A constructor with two numeric arguments (not counting self), that initializes the real and imag instance variables, respectively.
# get_real:returns the real component of the complex number
# get_imag:returns the imaginary component of the complex number
# set_real:sets the real component to the new value
# set_imag:set the imaginary component to the new value
# __str__:overloads the str method so that it returns the approiate string
# __add__:overloads the + method so that it returns the approiate addition
# __mul__:overloads the * method so that it returns the correct *
# __eq__:overloads the == method so that it returns True or false if values are equal
#==========================================

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
        
    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imag

    def set_real(self,new_real):
        self.real=new_real

    def set_imag(self,new_imag):
        self.imag=new_imag

    def __str__(self):
        return str(self.real)+' + '+str(self.imag)+'i'

    def __add__(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)

    def __mul__(self,other):
        return Complex(self.real*other.real-self.imag*other.imag,self.real*other.imag+self.imag*other.real)
    def __eq__(self,other):
        if self.real==other.real and self.imag==other.imag:
            return True
        else:
            return False

#item===================================
# Purpose: contains the things pertaining to items to be potentially purchased
# Instance variables:
# name-represents the name of the product
# price-represents the price of the product
# category-represents the category the product relates to
# store-represents the store the product can be found at
# Methods:
# __init__:A constructor that initializes the previously mentioned variables.
# __str__:overloads the str method so that it returns the approiate string
# __lt__:overloads the < method so that it returns True or false if price of first related to second
#==========================================
class Item:
    def __init__(self,name,price,category,store):
        self.name=name
        self.price=float(price)
        self.category=category
        self.store=store
    def __str__(self):
        return str(self.name)+', '+str(self.category)+', '+str(self.store)+': $'+str(self.price)
    def __lt__(self,other):
        if self.price<other.price:
            return True
        else:
            return False
#store===================================
# Purpose: contains the things pertaining to store where items can be purchased
# Instance variables:
# name-represents the name of the product
# price-represents the price of the product
# category-represents the category the product relates to
# store-represents the store the product can be found at
# self.items-stores the list of items into itself
# self.tracker-stores how many items in the store there is for future use
# Methods:
# __init__:A constructor that initializes the previously mentioned variables.
# __str__:overloads the str method so that it returns the approiate string
#==========================================
class Store:
    def __init__(self,name,filename):
        self.name=name
        fname=open(filename)
        self.items=[]
        line=fname.readline()
        self.tracker=0
        for i in fname:
            lst=i.split(',')
            if '\n' in lst[2]:
                self.items.append(Item(lst[0],lst[1],lst[2][0:-1],self.name))
            else:
                self.items.append(Item(lst[0],lst[1],lst[2],self.name))
            self.tracker+=1
        fname.close()
    def __str__(self):
        returning=self.name+'\n'
        for i in range(self.tracker):
            returning+=str(self.items[i])+'\n'
        return returning

    
def cheap_outfit(store_list):
    cheapskate={'Head':101,'Torso':101,'Legs':101,'Feet':101} #note, since given $100, max price any 1 object could be is 100
    cheapskate_item={'Head':101,'Torso':101,'Legs':101,'Feet':101}
    for i in store_list:
        for j in range(i.tracker):
            checking=i.items[j].category
            if float(i.items[j].price)<=float(cheapskate[checking]):
                cheapskate[checking]=i.items[j].price
                cheapskate_item[checking]=i.items[j]
        
    return cheapskate_item
