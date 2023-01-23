from silnik import Silnik
from akumulator import Akumulator
from skrzynia_biegow import skrzyniabiegow
from miejsca import Czlonkowie
class Auto:
    def __init__(self, wlasciciel : str) -> None:
        self.__wlascicel = wlasciciel
        self.__akumlator = Akumulator()
        self.__silnik = Silnik()
        self.__skrzyniabiegow = skrzyniabiegow()
        self.__miejsca = Czlonkowie()

    def all_information(self):
        print("="*40)
        print(self.__wlascicel)
        self.__akumlator.informacje()
        self.__silnik.informacje()
        self.__skrzyniabiegow.informacje()
        self.__miejsca.info()
        print("="*40)

    def zmien_informacje(self):
        print("co chcesz zmienic")
        print("a - silnik")
        print("b - akumulator")
        print("c - skrzynia biegow")
        inp = input().lower().strip()
        if inp == "a":
            self.__silnik.zmien_informacje_silnik()
        elif inp == "b":
            self.__akumlator.zmien_dane_akumolatora()
        elif inp == "c":
            self.__skrzyniabiegow.zmieninfoskrzyniabiegow()

    def brrrbrrrr(self):
        self.__silnik.brrrbrrrr()
        