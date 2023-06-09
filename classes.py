#classes for player, and locations (locations should be nodes with 4 edges: north, south, east and west)


class person:
    def __init__(self):
        self.name = None
        self.inventory = {} #item.name:item
        self.location = ''
        self.minerals = 0

    



class location:
    def __init__(self):
        self.name = None  
        self.greeting = ''  #here we put the greeting along the lines of, you see a bank with a green window, to the west there is fog, and you are surrounded by a great brick wall from the north, east, and south
        self.inventory = {} #dict for all items that the player can PICK UP and add to their inventory item.name:item
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.attached = [self.north,self.south,self.east,self.west]
        self.hasmineral = None
        self.persons = {} #says who is in location     person.name:person


        

        # we need descriptinos for what is north south etc , especially for when we cant go in those directions

class item:
    def __init__(self,name): #to destroy the objects, trash array/dict????
        self.name = name
        
        
        self.isgone = None
        self.isalive = False
        self.interactables = {} #dict of items with which current item can interact with itemname:itemvar
        self.verbs = {}
        self.prepositions = []  #prepositions that are valid in command before item
        self.onpickup = "You picked up a {}".format(self.name) #append to string if you want more to happen
        self.ondrop = "You dropped the {}".format(self.name) #append to string if you want more to happen
        self.onpickupgreeting = None #message to add to location greeting after item gets pickedup
        self.directobjects = {} #




class NPC(person):
    def __init__(self,name):
        super().__init__(name)
        self.name = name

#instantiations, we must creater player controller object here
gamegoing = True
me = person()


#private methods ----------------------------------------------------------------


        




#ALL VERB METHODS GO BELOW : PUBLIC METHODS PRIVATE ABOVE

def pickup(item): #item is an object from item class

    

    #add item from location to inventory
    me.inventory[item.name] = me.location.inventory[item.name]

    #remove item from location
    me.location.inventory.pop(item.name)
    
    print(item.onpickup)

    if item.onpickupgreeting != None:
        me.location.greeting += item.onpickupgreeting

def drop(item):#arg is item object, drop item leaves player inventory enters current location inventory, inverse of pickup
    if item.name in me.inventory:
    #adds item object to current location inventory dictinoary item.name:item
        me.location.inventory[item.name] = me.inventory[item.name]

        #removes item from player inventory 
        me.inventory.pop(item.name)

        #print dropped message
        print(item.ondrop)
    
    else:
        print("You can't drop what you dont have :(")



def showinventory():
    if len(me.inventory) == 0:
        print("You have nothing in your inventory! ")
    else:
        for key in me.inventory:
            print(key)



#look method just reprints current location greeting:

def look():
    print(me.location.greeting)

def nullverb(): #this method is for verbs we want to recognize as reasonable but can not be done, 
                #for the sake of adding verb to verbs dictinoary:  'nullverb' : nullverb
    pass

def test_soil():

    #add case where person is there and therefore cannot drill


    if me.location.hasmineral == True:
        #remove mineral from location
        me.location.hasmineral = False
        print("You have tested and found this site suitable for excavation! Good job!")
        me.location.greeting += "You have tested and found this site suitable for excavation! Good job!"

        me.minerals += 1

        if me.minerals == 3:
            #have the win condition and other stuff happen
            pass

    else:
        print("ROVER:Either, this site is not suitable for excavation, or you have already tested and confirmed this site.")















#verbs are methods, all verbs should be defined above ----------------------------------------------------------------------------------------------

#need single verbs dictionary
singleverbs = {'inventory':showinventory,'look':look,'test_soil':test_soil}




#this should be a dictinoary 'verb':verb/method
verbs = {'pickup':pickup,'inventory':showinventory,'drop':drop}

#add singleverbs to verbs
verbs.update(singleverbs)