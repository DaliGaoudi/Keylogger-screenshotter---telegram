import telegram
import asyncio
import pyautogui
import time 

async def main():
    bot = telegram.Bot(token='6541175839:AAEdVSOXC5uGSr8CnnWHMnv_JhswKbbW5JY')
    async with bot:
        await bot.send_message(text="hello",chat_id=-4117162001)

#asyncio.run(main()) 
while True:
    time.sleep(5)        
    scr = pyautogui.screenshot(r'screenshot1.png')
