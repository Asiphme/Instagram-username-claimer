# run.py

import asyncio
import yaml
from claimer import InstagramClaimer
from proxy_manager import ProxyManager
from config import config

# Sozlamalarni o'qish
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Proxy manager yaratish
proxy_manager = ProxyManager(config['proxy']['sources'])

# Instagram claimer yaratish
claimer = InstagramClaimer(
    config=config,
    proxy_manager=proxy_manager
)

# Asinxron ishga tushirish
if __name__ == "__main__":
    asyncio.run(claimer.run())
