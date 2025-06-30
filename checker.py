from logger import logger

async def is_username_available(username, page):
    try:
        url = f"https://www.instagram.com/{username}/"
        await page.goto(url, timeout=10000)
        if "Page Not Found" in await page.content():
            logger.info(f"Username @{username} is available")
            return True
        else:
            logger.info(f"Username @{username} is taken")
    except Exception as e:
        logger.error(f"Error checking username {username}: {e}")
    return False
