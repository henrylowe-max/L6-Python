class Reproduction:
    LIVE = "birthing live young"
    EGGS = "laying eggs"

class BodyCover:
     FUR = "fur"
     FEATHERS = "feathers"
     SCALES = "scales"

class Animal:
    def __init__(self,bioClass:str,
                 species:str,
                 reproduce:str,
                 hasMilk:bool,
                 bodyCover:str):
        
        self.__bioClass = bioClass
        self.__species = species
        self.__reproducesBy = reproduce
        self.__milkSuckle = hasMilk
        self.__bodyCover = bodyCover
        self._protected = None


    def __str__(self):
        value =  f"Animal Class  : {self.__bioClass}\n"
        value += f"Reproduces By : {self.__reproducesBy}\n"
        value += f"Suckles Milk  : {self.__milkSuckle}\n"

        return value
       
      



def testAnimal():
    vulture = Animal("Bird","Aves",Reproduction().EGGS,False,BodyCover().FEATHERS)

    try:
        vulture._protected = "I set this - naughty!"
    except Exception as e:
        print(f"Error {e}")
    else:
        print(f"protected changed: {vulture._protected}")

    try:
        vulture.__milkSuckle = True
    except Exception as e:
            print(f"Error {e}")
    else:
            print(f"I changed private: {vulture.__milkSuckle}")
    
    print(vulture)   


class Pet(Animal):
    def __init__(self,
                 bioClass:str,
                 species:str,
                 reproduce:str,
                 hasMilk:bool,
                 bodyCover:str,
                 owner:str,
                 name:str):
        #Call the Parents constructor
        super().__init__(bioClass,species,reproduce,hasMilk,bodyCover)
        self.__owner = owner
        self.__name =  name

    def __str__(self):
        value = super().__str__() # call parents __str__()
        value += f"My owner is {self.__owner}\n "
        value += f"My name is {self.__name}\n "

        return value

    # Getter Methods
    def getOwner(self):
        return self.__owner

    def getName(self):
        return self.__name

    #setter methods
    def changeOwner(self,newOwner:str):
        self.__owner = newOwner

    def changeName(self,newName:str):
        self.__name = newName

def testPet():
    goldfish = Pet("Actinopterygii",
                     "Carassius auratus",
                     Reproduction.EGGS,
                     False,
                     BodyCover.SCALES,
                     "John Arbuckle",
                     "Goldie"
                     )    

    print(goldfish)
    try:
        goldfish.__name = "Fred"
    except Exception as e:
        print(f"Error {e}")
    else:
        print("changed goldfish.__name attribute")
    print("However these are not actually set!")
    print(goldfish)

class Dog(Pet):
    def __init__(self,owner:str,name:str,breed:str):
        super().__init__("Mammal",
                         "Canis Lupis",
                         Reproduction.LIVE,
                         True,
                         BodyCover.FUR,
                         owner,
                         name
                         )
        self.__breed = breed

    def __str__(self):
        value = super().__str__()
        value += f". and I am a {self.__breed}"
        return value

class Cat(Pet):
    def __init__(self,owner:str,name:str,breed:str):
        super().__init__("Mammal",
                         "Felis catus",
                         Reproduction.LIVE,
                         True,
                         BodyCover.FUR,
                         owner,
                         name
                         )
        self.__breed = breed

    def __str__(self):
        value = super().__str__()
        value += f". and I am a {self.__breed}"
        return value

def johnsPets():
    garfield = Cat("John Arbucle",
                   "Garfield",
                   "Mancoon Moggy")
    odi = Dog("John Arbucle",
              "Odi",
              "Mongrell")

    print(garfield)
    print(odi)

    
if __name__ == "__main__":
    testAnimal()
    print("-"*10)
    testPet()
    print("-"*10)
    johnsPets()