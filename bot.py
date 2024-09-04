import telegram
import asyncio
import pyautogui
import time 

async def main():
    bot = telegram.Bot(token='your_telegram_bot_token')
    async with bot:
        await bot.send_message(text="hello",chat_id=-4117162001)

#asyncio.run(main()) 
while True:
    time.sleep(5)        
    scr = pyautogui.screenshot(r'screenshot1.png')
