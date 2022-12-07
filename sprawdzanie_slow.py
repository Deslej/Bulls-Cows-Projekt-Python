import random
class Dictionary:
    def __init__(self):
        try:
            with open("dictionary.txt","r") as file:
                self.baza=[x for x in file.read().split()]
                if len(self.baza)<10:
                    print("Za mało słow w pliku dictionary.txt")
                    exit(1)
        except FileNotFoundError:
            print("Nie ma takiego pliku")
    def wybor_slowa_trudnosc(self,poziom):
        if poziom==1:
            łatwy=[słowo for słowo in self.baza if len(słowo) <= 4]
            return random.choice(łatwy)
        elif poziom==2:
            średni = [słowo for słowo in self.baza if len(słowo) >4 ]
            średniv2=[słowo for słowo in średni if len(słowo) <=7]
            return random.choice(średniv2)
        elif poziom==3:
            trudny= [słowo for słowo in self.baza if len(słowo) > 7]
            return random.choice(trudny)
class Validator:
    def jest_izogramem(self,string):
        string = string.lower()
        for char in string:
            if string.count(char) > 1:
                return False
        return True
