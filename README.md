# 📛 Instagram Username Claimer

**Automated Instagram username checker and claimer using Playwright, proxies, and Telegram bot.**

---

## 🔧 Features

- ✅ Check available Instagram usernames
- ⚡ Automatically claim available usernames
- 🌐 Proxy rotation and management
- 🤖 Telegram notifications for successful claims
- 🧠 CAPTCHA solving with 2Captcha

---

## 🚀 Technologies Used

- Python 3
- [Playwright](https://playwright.dev/python/)
- [2Captcha API](https://2captcha.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- Proxy support (HTTP/SOCKS)

---

## 📂 Project Structure

```
├── claimer.py           # Core logic for claiming
├── checker.py           # Username availability checker
├── captcha_solver.py    # 2Captcha integration
├── proxy_manager.py     # Proxy management
├── config.yaml          # Configurable settings
├── logger.py            # Logging utilities
├── utils.py             # Helper functions
├── run.py               # Entry point
├── requirements.txt     # Python dependencies
└── banned_proxies.txt   # Automatically filtered bad proxies
```

---

## ⚙️ Configuration

1. Edit your `config.yaml` file:

```yaml
telegram:
  bot_token: YOUR_BOT_TOKEN
  chat_id: YOUR_CHAT_ID

captcha:
  api_key: YOUR_2CAPTCHA_API_KEY

proxies:
  file: proxies.txt
```

2. Add your proxy list to `proxies.txt`.

---

## 🧪 Usage

```bash
pip install -r requirements.txt
python run.py
```

---

## 📬 Telegram Alerts

You’ll receive real-time updates like:

```
✅ Claimed: @cool_username
```

---

## 🛡 Disclaimer

> This tool is for **educational and ethical purposes** only.  
> Do **not** use it to violate Instagram's Terms of Service or for malicious activity.

---

## ⭐ Contribute

Pull requests are welcome. If you find issues, feel free to open an issue or PR.

---
