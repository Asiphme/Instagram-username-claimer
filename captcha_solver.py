import requests
import time
from logger import logger
from config import config

class CaptchaSolver:
    def __init__(self):
        self.api_key = config['captcha']['api_key']

    def solve_hcaptcha(self, sitekey, url):
        try:
            logger.info("Submitting CAPTCHA to 2Captcha")
            r = requests.post("http://2captcha.com/in.php", data={
                'key': self.api_key,
                'method': 'hcaptcha',
                'sitekey': sitekey,
                'pageurl': url,
                'json': 1
            })
            captcha_id = r.json().get("request")
            time.sleep(20)

            for _ in range(20):
                res = requests.get(f"http://2captcha.com/res.php?key={self.api_key}&action=get&id={captcha_id}&json=1")
                if res.json().get("status") == 1:
                    return res.json().get("request")
                time.sleep(5)
        except Exception as e:
            logger.error(f"Captcha solving error: {e}")
        return None
