import time
from datetime import datetime

def hesaplayıcı():
	try:
		print("\n")
		baslangıcsaat = input('Not : Başlangıç Saatini Saat.Dakika Olarak Gir(12.30)\nBaşlangıç Saatini Gir : ')
		print("\n")
		baslangıcayrac = baslangıcsaat.split(".")

		gun=datetime.now().strftime('%d')
		ay=datetime.now().strftime('%m')
		yıl=datetime.now().strftime('%Y')

		a = datetime(int(yıl), int(ay), int(gun), int(baslangıcayrac[0]), int(baslangıcayrac[1]))
		#a = datetime(2022, 11, 27, 1, 40,30)
		b = datetime.now()
		gecensure = round(((b-a).seconds)/60)
		if gecensure>720:
			print("Geçen Süre  =  ",gecensure-720, "Dakika")
			print("\n")
			print("ÜCRET = *** ",round((gecensure-720)*(0.333333)),"TL ***\n")
		else:
			print("Geçen Süre  =  ",gecensure, "Dakika")
			print("\n")
			print("ÜCRET = *** ",round(gecensure*(0.333333)),"TL *** \n")
	except ValueError:
		print("\tHATA : SAATİ DÜZGÜN YAZ (SAAT İLE DAKİKANIN ARASINA .NOKTA KOY)")
	except IndexError:
		print("\tHATA : Saat ile dakikayı düzgün yaz")
		

while True:
	hesaplayıcı()