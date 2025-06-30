import asyncio
from logger import logger
from checker import is_username_available
from captcha_solver import CaptchaSolver
from proxy_manager import ProxyManager
from playwright.async_api import async_playwright
from config import config
from utils import send_telegram_message, username_generator

class InstagramClaimer:
    def __init__(self, config, proxy_manager):
        self.proxy_manager = ProxyManager(config['proxy']['sources'])
        self.captcha_solver = CaptchaSolver()

    async def claim_username(self, username):
        proxy = self.proxy_manager.get_proxy()
        logger.info(f"Trying to claim: {username} using proxy {proxy}")
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context(proxy={"server": f"http://{proxy}"} if proxy else None)
                page = await context.new_page()
                
                # Hozircha faqat tekshiruv
                available = await is_username_available(username, page)
                if available:
                    send_telegram_message(f"✅ Username claimed: @{username}")
                    with open("available.txt", "a") as f:
                        f.write(username + "\n")
                
                await context.close()
                await browser.close()
        except Exception as e:
            logger.error(f"Error claiming {username}: {e}")
            if proxy:
                self.proxy_manager.ban_proxy(proxy)

    async def run(self):
        usernames = username_generator(
            min_length=config['settings']['min_username_length'],
            max_length=config['settings']['max_username_length'],
            include_numbers=config['settings']['include_numbers']
        )
        tasks = []
        for username in usernames:
            tasks.append(asyncio.create_task(self.claim_username(username)))
            if len(tasks) >= config['settings']['threads']:
                await asyncio.gather(*tasks)
                tasks = []
