import datetime
class Przechowywanie:
    def __init__(self):
        self.b=[]
        self.c=[]
class Stats:
    def __init__(self,pr):
        self.cows=0
        self.bulls=0
        self.proby=pr
    def eksport_wyniku(self):
        with open("highscores.txt", "a") as file:
            file.write(f"Data:{datetime.datetime.now()},cows:{self.cows},bulls:{self.bulls},proby{self.proby}\n")
    def zwieksz_bulls(self):
        self.bulls=self.bulls+1
    def zwieksz_cows(self):
        self.cows=self.cows+1
    def zmniejsz_proby(self):
        self.proby=self.proby-1
    def resetowanie_stat(self):
        self.cows=0
        self.bulls=0
