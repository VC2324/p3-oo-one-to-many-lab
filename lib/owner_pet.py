class Pet:

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all =[]

    def __init__(self, name, pet_type, owner=None ):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if pet_type not in self.PET_TYPES:
            raise Exception("INVALID PET TYPE")
       
class Owner:
    def __init__(self, name):
        self.name =  name
        self.all = []

    def pets(self):
        return self.all

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner =self
            self.all.append(pet)
        else:
            raise Exception("Invalid pet Object")

   

    # def add_pet(self, pet):
    #     if isinstance(pet, Pet):
    #         pet.owner = self
    #         self.allpets.append(pet)
    #     else:
    #         raise Exception("Invalid pet object")
    