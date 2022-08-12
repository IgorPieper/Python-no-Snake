import requests

# ----------------- CONS ------------------- #

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
UP_ARROW = "🔺"
DOWN_ARROW = "🔻"

ALPHAVENTAGE_KEY = "Your Code"
NEWS_API_KEY = "Your Code"

# ----------------- CONN TO ALPHAVENTAGE ------------------- #

# ALPHAVENTAGE Documentation = https://www.alphavantage.co/documentation/

alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVENTAGE_KEY,
}

response_alpha = requests.get(url="https://www.alphavantage.co/query", params=alpha_params)
response_alpha.raise_for_status()

# ----------------- TAKING STOCK DATA ------------------- #

data = response_alpha.json()["Time Series (Daily)"]
day_list = [key for key in data]
yesterday_closing_price = float(data[day_list[0]]["4. close"])
day_before_yesterday_closing_price = float(data[day_list[1]]["4. close"])

# ----------------- PERCENT CALC ------------------- #

difference = yesterday_closing_price - day_before_yesterday_closing_price
fall_or_rise = ""
if difference > 0:
    fall_or_rise = UP_ARROW
else:
    fall_or_rise = DOWN_ARROW
diff_percent = (abs(difference) / yesterday_closing_price) * 100
rounded_diff_perc = int(diff_percent)

# ----------------- CONN TO NEWS API ------------------- #

# NEWS API Documentation = https://newsapi.org/docs

news_params = {
    "q": STOCK,
    "apiKey": NEWS_API_KEY,
}

response_news = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
response_news.raise_for_status()

# ----------------- TAKING NEWS ------------------- #

news_data = response_news.json()["articles"]
for n in range(0, 3):
    title = news_data[n]["title"]
    description = news_data[n]["description"]

    # ----------------- SHOW RESULTS ------------------- #

    print(f"\n{STOCK}: {fall_or_rise}{rounded_diff_perc}%")
    print(f"Headline: {title}")
    print(f"Brief: {description}\n")
