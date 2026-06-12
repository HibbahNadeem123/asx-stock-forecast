import yfinance as yf #using Yahoo Finance servers to download the stock data
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("data", exist_ok=True)

TICKERS = ["BHP.AX", "CBA.AX", "CSL.AX", "NAB.AX", "WES.AX"]

raw = yf.download(TICKERS, period="5y", interval="1d", auto_adjust=True)

cba= raw["Close"]["CBA.AX"].dropna()
cba.to_csv("data/cba_close.csv")

plt.figure(figsize=(12,5))
plt.plot(cba.index, cba.values, linewidth=1, color="#185FA5")
plt.title("CBA.AX - Closing price (5 years")
plt.xlabel("Date")
plt.ylabel("AUD")
plt.tight_layout()
plt.savefig("data/cba_chart.png",dpi=150)
plt.show()
