
# 📊 Gap-Up Strategy Analysis App

This project is a full-stack trading system that analyzes and automates a **Gap-Up Trading Strategy**. It includes real-time **Telegram alerts** whenever a trade is executed or failed, so users stay informed even without opening the dashboard.

---

## 🧩 Tech Stack

| Layer         | Tech                         |
| ------------- | ---------------------------- |
| UI Dashboard  | Streamlit                    |
| Scheduling    | AWS Lambda + CloudWatch Cron |
| Broker API    | Fyers API                    |
| Data Storage  | MongoDB Atlas                |
| Notifications | Telegram Bot                 |
| Language      | Python                       |

---

## 🔄 Trading Flow

1. **AWS Lambda Cron** triggers strategy at market open.
2. **Strategy checks** gap-up conditions and places trades via **Fyers API**.
3. **PNL and trade data** is saved in **MongoDB Atlas**.
4. **Telegram bot** sends trade execution alerts.
5. **Streamlit app** displays historical PNL and stats.

---

## 📢 Telegram Alerts Integration

### ✅ What It Does

* Sends message for:

  * Trade executed (buy/sell)
  * Trade skipped (gap condition not met)
  * Any execution error (for debugging)
* Real-time alerts to your Telegram account or group.

### 🔧 Setup

1. **Create Telegram Bot**

   * Talk to [@BotFather](https://t.me/BotFather)
   * Use `/newbot` to create a bot and get `BOT_TOKEN`

2. **Get Chat ID**

   * Send message to your bot
   * Use this URL to get chat ID:

     ```
     https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
     ```
   * Note down your `chat_id`

3. **Code Example (`telegram_alert.py`)**:

```python
import requests

def send_telegram_alert(message, bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        res = requests.post(url, json=payload)
        return res.status_code == 200
    except Exception as e:
        print("Failed to send Telegram alert:", e)
        return False
```

4. **Use in Strategy Execution**:

```python
from telegram_alert import send_telegram_alert

# Example alert after placing a trade
send_telegram_alert(
    f"📈 Trade Executed:\nSymbol: {symbol}\nSide: BUY\nPrice: {entry_price}",
    bot_token="YOUR_BOT_TOKEN",
    chat_id="YOUR_CHAT_ID"
)
```

---

## 📁 Repository Setup

In GitHub's "Edit repository details":

* **Description**:

  ```
  Automated Gap-Up Trading Strategy with Fyers API, Streamlit, AWS Lambda, and Telegram alerts
  ```
* **Topics**:

  ```
  trading fyers-api telegram-alerts streamlit aws-lambda mongodb
  ```

---

## 🔐 Security Tips

* Store `BOT_TOKEN`, `chat_id`, Fyers token, Mongo URI securely using:

  * `.env` + `python-dotenv`
  * AWS Secrets Manager (for Lambda)

---

## 📈 Future Enhancements

* Add interactive controls to execute backtests
* Notify via Telegram on:

  * Daily summary
  * Unexpected losses
* Add retry logic for order failures
* Telegram command support (e.g., `/pnl`, `/last_trade`)

