# 📊 Gap-Up Strategy Analysis App

This project is a full-stack trading analytics and strategy execution platform that allows users to analyze and automate a **Gap-Up Trading Strategy** using:

* **Streamlit** frontend
* **MongoDB** for data storage
* **AWS Lambda + Cron** for scheduled strategy execution
* **Fyers Broker API** to place trades and fetch market data

---

## 📁 Project Structure

```
trading-strategy-app/
│
├── streamlit_app.py           # Streamlit frontend app
├── strategy_logic.py          # Trading logic (for AWS Lambda)
├── fyers_helper.py            # Helper functions to interact with Fyers API
├── requirements.txt           # Python dependencies
├── deploy_lambda.sh           # Script to deploy to AWS Lambda (optional)
└── README.md                  # Project documentation (this file)
```

---

## 🧠 Strategy Overview: Gap-Up Trading

This strategy aims to take advantage of **gap-up openings** — when a stock opens significantly higher than its previous day’s close.

* **Entry**: If the stock opens with a gap-up beyond a threshold (e.g., >1% gap).
* **Exit**: Exit by EOD or based on profit/loss conditions.
* **Log PNL**: Store PNL in MongoDB after each execution.

---

## 💻 Technologies Used

| Layer              | Tech                           |
| ------------------ | ------------------------------ |
| Frontend           | Streamlit                      |
| Backend            | Python                         |
| Scheduler          | AWS Lambda + CloudWatch (Cron) |
| Data Storage       | MongoDB Atlas                  |
| Broker Integration | Fyers API                      |

---

## 🔧 Streamlit App (`streamlit_app.py`)

### Key Features:

* Visualizes **cumulative PNL**
* Shows **data table** of trades
* Displays **insights** like avg, max, min PNL
* Refresh button to reload latest data

### Run locally:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 🔄 Strategy Execution (Lambda + Cron)

### `strategy_logic.py`

Contains:

* Authentication with Fyers
* Fetching stock data
* Applying the gap-up strategy
* Calculating and logging PNL
* Inserting the result into MongoDB

### Deploying to AWS Lambda:

1. Zip `strategy_logic.py`, `fyers_helper.py`, and dependencies
2. Upload to Lambda
3. Set IAM role for VPC + secrets
4. Schedule using **CloudWatch Events (cron)**

Example cron for 9:15 AM IST (Indian Market Open):

```bash
cron(45 3 ? * MON-FRI *)  # 3:45 UTC = 9:15 IST
```

---

## 🔗 Fyers Broker API Integration (`fyers_helper.py`)

Handles:

* Login via OAuth2
* Token management
* Placing orders
* Fetching historical/market data

👉 Make sure to:

* Register your redirect URI with Fyers
* Store `access_token` securely (consider AWS Secrets Manager)

---

## 🌐 MongoDB (Atlas)

* Used to store each trade’s date and PNL.
* Collection: `Pnl_Gap`
* Fields: `{ Date, PNL }`

MongoDB connection URI used in `streamlit_app.py` and `strategy_logic.py`.

---

## 🛡️ Security

* Do not hardcode secrets in code.
* Use `.env` or AWS Secrets Manager.
* Apply CORS, token expiration checks if hosting Streamlit online.

---

## 📈 Future Improvements

* Add more strategies (e.g., Gap-Down, Momentum)
* Daily email reports using SES
* Telegram bot alerts
* Add auth login to Streamlit app
* Store logs and trades in detailed format

---

## ✅ Example Use-Case Flow

1. **9:15 AM**: Lambda triggers and executes strategy
2. Fetches market data via Fyers
3. Applies logic and places order
4. Calculates PNL and inserts into MongoDB
5. **Later**: User opens Streamlit app to view performance

---

## 📦 `requirements.txt` Example

```txt
pandas
numpy
streamlit
matplotlib
pymongo
fyers-apiv2
requests
```

