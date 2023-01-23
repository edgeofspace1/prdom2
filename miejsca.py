class Czlonkowie:
	def __init__(self):
		self.__lczba_miejsc = None
		self.__liczba_pasazerow = None
		self.__zmianadanepasazer = None
		self.__zmiendanemiejsc = None
		
	def info(self):
		print("Dane o miejscach")
		print("Liczba miejsc", self.__lczba_miejsc)
		print("Liczba pasazerow", self.__liczba_pasazerow)
		print("Liczba pasazerow", self.__zmiendanemiejsc)

	