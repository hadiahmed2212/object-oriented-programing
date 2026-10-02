class Pet:
    print("im a class for a pet!")
pet_obj= Pet()

class PetP:

    category= "pet"

    def __init__(self,name,anity,age,favourite_food):
        self.name = name
        self.animal=anity
        self.age=age
        self.favourite_food=favourite_food
pet1= PetP("snowy","parrot",7,"seeds")
pet2= PetP("bluey","parrot",5,"sunflower_seeds" )

print(f"snowy is a {pet1}".format(pet1.category))
print(f"bluey is a {pet2}".format(pet2.category))