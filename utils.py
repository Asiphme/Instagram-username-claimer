import random
import string
import requests
from config import config

def username_generator(min_length=3, max_length=5, include_numbers=True):
    characters = string.ascii_lowercase
    if include_numbers:
        characters += string.digits

    return [''.join(random.choices(characters, k=random.randint(min_length, max_length)))
            for _ in range(5000)]

def send_telegram_message(message):
    bot_token = config['telegram']['bot_token']
    chat_id = config['telegram']['chat_id']
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    try:
        requests.post(url, data={'chat_id': chat_id, 'text': message})
    except Exception as e:
        print(f"Telegram error: {e}")
