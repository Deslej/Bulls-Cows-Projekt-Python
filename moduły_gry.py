from sprawdzanie_slow import *
from staty import *
from time import sleep
class Engine:
    def __init__(self):
        self.domyslna_ilosc_prob=10
        self.staty=Stats(self.domyslna_ilosc_prob)
        self.wyrazy= Dictionary()
        self.izogram= Validator()
        self.przecho= Przechowywanie()
        self.trudnosc=1

    def zmiana_trudnosci_gry(self):
        print("wybierz poziom trudnosci gry:\n"
              "1.latwy\n"
              "2.sredni\n"
              "3.trudny\n")
        x=int(input())
        if x >= 1 or x <= 3:
            self.trudnosc=x
        else:
            print("nie mozemy zmienic trudnosci\n")

    def zmiana_liczby_prob(self):
        print("Podaj ile chcesz miec prob na odgadniecie wyrazu:\n")
        z=int(input())
        if z>=1:
            self.domyslna_ilosc_prob=z
            self.staty.proby=z
        else:
            print("wybrałeś za niska liczbe prob!!!!\n"
                  "wartosc prob jest znowu 10\n")
            self.domyslna_ilosc_prob=10
            self.staty.proby = 10

    def sprawdzanie_slowa(self,twoje_slowo,słowo):
        for(twoje_znak,słowo_znak) in zip(twoje_slowo,słowo):
            if twoje_znak in słowo:
                if twoje_znak == słowo_znak:
                    self.przecho.b.append(twoje_znak)
                    self.staty.zwieksz_bulls()
                else:
                    self.przecho.c.append(twoje_znak)
                    self.staty.zwieksz_cows()
        print(f"Bulls:{self.przecho.b} Cows:{self.przecho.c}")
        self.przecho.c.clear()
        self.przecho.b.clear()
        return self.staty.bulls ,self.staty.cows

    def sprawdzanie_zgadywania(self,słowo):
        if self.staty.bulls==len(słowo):
            return True
        else:
            self.staty.zmniejsz_proby()
            return False

    def start(self):
        print(self.trudnosc)
        słowo = self.wyrazy.wybor_slowa_trudnosc(self.trudnosc)
        print(f"Dlugosc slowa wybranego przez komputer to:{len(słowo)}\n")
        self.staty.proby = self.domyslna_ilosc_prob
        while self.domyslna_ilosc_prob > 0:
            self.staty.resetowanie_stat()
            twoje_slowo=input()
            if self.izogram.jest_izogramem(twoje_slowo):
                Engine.sprawdzanie_slowa(self,twoje_slowo,słowo)
            else:
                print("twoje słowo nie jest izogramem\n")
            wartosc_zgadywania=Engine.sprawdzanie_zgadywania(self,słowo)
            if wartosc_zgadywania:
                print("zgadłes dobrze\n"
                      f"Tyle prob ci zostało:{self.staty.proby}\n")
                break
            else:
                if self.staty.proby==0:
                    print("Przegrałes\n")
                    print(f"{słowo}")
                    break
                else:
                    print("złe słowo\n"
                          f"Bulls:{self.staty.bulls},Cows:{self.staty.cows},Proby:{self.staty.proby}\n")




def menu():
    print("WITAJ W GRZE BULLS AND COWS\n"
          "1.Nowa gra\n"
          "2.Zasady gry\n"
          "3.Zmiana liczby prób\n"
          "4.Zmiana trudnosci gry\n"
          "5.Eksport wynikow\n"
          "6.koniec\n")
def zasady():
    print("Tekstowa gra w ktorej komputer losuje słowo,ktore jest izogramem i informuje uzytkownika o ilosci liter w slowie.\n"
          "Uzytkownik stara sie zgadnac co to za slowo.Komputer po kazdej probie zwraca liczbe Bulls and Cows.\n"
          "Liczba przy slowie Cows oznacza litere wystepujaca w slowie lecz na zlej pozycji,liczba przy slowie Bulls\n"
          "oznacza poprawna litere na poprawnej pozycji.Gra konczy sie kiedy liczba przy Bulls bedzie taka sama jak\n"
          "dlugosc slowa wylosowanego przez komputer.\n")

def menu_do_odpalenia(Engine):
    menu()
    wybor_uzytkownika=int(input())
    while wybor_uzytkownika > 6 or wybor_uzytkownika <1:
        print("wybierz numer z menu")
        wybor_uzytkownika = int(input())
    else:
        if wybor_uzytkownika==1:
            Engine.start()
        elif wybor_uzytkownika==2:
            zasady()
        elif wybor_uzytkownika==3:
            Engine.zmiana_liczby_prob()
        elif wybor_uzytkownika==4:
            Engine.zmiana_trudnosci_gry()
        elif wybor_uzytkownika==5:
            Engine.staty.eksport_wyniku()
        elif wybor_uzytkownika==6:
            exit(1)



