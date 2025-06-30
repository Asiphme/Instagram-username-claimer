import requests
import random
from logger import logger
from utils import send_telegram_message  # Telegramga xabar yuborish uchun

class ProxyManager:
    def __init__(self, sources, telegram_config=None):
        self.sources = sources
        self.telegram_config = telegram_config
        self.proxies = set()
        self.good_proxies = set()
        self.bad_proxies = set()
        self.load_proxies()

    def load_proxies(self):
        logger.info("Loading proxies...")
        for url in self.sources:
            try:
                response = requests.get(url, timeout=10)
                for line in response.text.splitlines():
                    proxy = line.strip()
                    if proxy and self.validate_format(proxy):
                        if self.test_proxy(proxy):
                            logger.info(f"Accepted proxy: {proxy}")
                            self.good_proxies.add(proxy)
                        else:
                            logger.warning(f"Rejected proxy (failed test): {proxy}")
                            self.ban_proxy(proxy)
            except Exception as e:
                logger.error(f"Failed to load proxies from {url}: {e}")
        logger.info(f"{len(self.good_proxies)} working proxies loaded.")
        if self.telegram_config:
            self.notify_working_proxies()

    def validate_format(self, proxy):
        return ':' in proxy and len(proxy.split(':')) == 2

    def get_proxy(self):
        available = list(self.good_proxies - self.bad_proxies)
        if not available:
            logger.warning("No valid proxies available.")
            return None
        return random.choice(available)

    def ban_proxy(self, proxy):
        if proxy not in self.bad_proxies:
            logger.warning(f"Banning bad proxy: {proxy}")
            self.bad_proxies.add(proxy)
            with open("banned_proxies.txt", "a") as f:
                f.write(proxy + "\n")

    def test_proxy(self, proxy):
        try:
            proxies = {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}",
            }
            resp = requests.get("https://www.instagram.com", proxies=proxies, timeout=7)
            if resp.status_code == 200:
                server_header = resp.headers.get("Server", "")
                cf_ray = resp.headers.get("cf-ray", "")
                if "cloudflare" in server_header.lower() or cf_ray:
                    return True
            return False
        except:
            return False

    def notify_working_proxies(self):
        message = "✅ *Working Proxies Loaded:*\n\n" + "\n".join(list(self.good_proxies)[:20])
        try:
            send_telegram_message(self.telegram_config['bot_token'], self.telegram_config['chat_id'], message)
            logger.info("Working proxies sent via Telegram.")
        except Exception as e:
            logger.error(f"Failed to send proxies to Telegram: {e}")
