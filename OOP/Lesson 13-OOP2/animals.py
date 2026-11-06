class Reproduction:
    LIVE = "birthing live young"
    EGGS = "laying eggs"

class BodyCover:
     FUR = "Fur"
     FEATHERS = "feathers"
     SCALES = "scales"

class Animal:
    def __init__(self,
                 bioClass:str,
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
        value  = f"Animal Class   : {self.__bioClass}\n"
        value += f"reproduces by  : {self.__reproducesBy}\n"
        value += f"species        : {self.__species}\n"
        value += f"has milk?      : {self.__milkSuckle}\n"
        value += f"has body cover : {self.__bodyCover}\n"
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
        print(f"private changed: {vulture.__milkSuckle}")
    
    
    print(vulture)


class Pet(Animal):
    def __init__(self,bioClass:str,species:str,reproduce:str,hasMilk:bool,bodyCover:str,owner:str,name:str):\
        
        super().__init__(bioClass,species,reproduce,hasMilk,bodyCover,owner,name)
        self.__owner = owner
        self.__name = name
        
    def __str__(self):
        value += super().__str__()
        value += f"my owner is called: {self.__owner}"
        value += f"my name is: {self.__name}"
        


if __name__ == "__main__":
    testAnimal()