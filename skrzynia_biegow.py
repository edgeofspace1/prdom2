class skrzyniabiegow:
    
    def __init__(self):
        self.__zmienbieg = None
        self.__automat = None
        self.__zmaianamocy = None
    
    def informacje(self):
        print("Dane Skrzyni Biegów")
        print(self.__zmienbieg)
        print(self.__automat)
        print(self.__zmaianamocy)


    def zmieninfoskrzyniabiegow(self):
        while True:
            print("k - zmien bieg")
            print("a - automatyczna")
            print('z - zmiana mocy')
            print("e - wyjscie")
            inp = input().lower().strip()
            if inp == "k":
                inp = input().lower().strip()
                self.__zmienbieg
            if inp == "a":
                inp = input().lower().strip()
                self.__automat = inp
            if inp == "z":
                inp = input().lower().strip()
                self.__zmaianamocy = inp
            if inp == "e":
                break  