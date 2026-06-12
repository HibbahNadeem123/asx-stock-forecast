import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV we saved in the last script
cba = pd.read_csv("data/cba_close.csv", index_col=0, parse_dates=True)
cba.columns = ["Close"]

print("=== Basic Info ===")
print(f"Date range: {cba.index.min().date()} to {cba.index.max().date()}")
print(f"Total Trading Days: {len(cba)}")

print("\n=== PRICE STATISTICS ===")
print(f"Lowest price:  AUD ${cba['Close'].min():.2f}")
print(f"Highest price: AUD ${cba['Close'].max():.2f}")
print(f"Average price: AUD ${cba['Close'].mean():.2f}")
print(f"Current price: AUD ${cba['Close'].iloc[-1]:.2f}")

print("\n=== VOLATILITY ===")
cba["Daily Return"] = cba["Close"].pct_change() * 100
print(f"Average daily move: {cba['Daily Return'].mean():.3f}%")
print(f"Biggest single day gain:  {cba['Daily Return'].max():.2f}%")
print(f"Biggest single day drop: {cba['Daily Return'].min():.2f}%")

# Plot 3 charts stacked
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Chart 1 - closing price with 30 and 90 day moving averages
cba["MA30"] = cba["Close"].rolling(30).mean()
cba["MA90"] = cba["Close"].rolling(90).mean()
axes[0].plot(cba.index, cba["Close"], linewidth=1, color="#B5D4F4", label="Close")
axes[0].plot(cba.index, cba["MA30"], linewidth=1.5, color="#185FA5", label="30-day avg")
axes[0].plot(cba.index, cba["MA90"], linewidth=1.5, color="#712B13", label="90-day avg")
axes[0].set_title("Closing price + moving averages")
axes[0].set_ylabel("AUD")
axes[0].legend()

# Chart 2 - daily returns
axes[1].bar(cba.index, cba["Daily Return"], color="#9FE1CB", width=1)
axes[1].axhline(0, color="#0F6E56", linewidth=0.8)
axes[1].set_title("Daily % change")
axes[1].set_ylabel("% change")

# Chart 3 - 30 day rolling volatility
cba["Volatility"] = cba["Daily Return"].rolling(30).std()
axes[2].plot(cba.index, cba["Volatility"], linewidth=1, color="#D85A30")
axes[2].set_title("30-day rolling volatility")
axes[2].set_ylabel("Std dev of returns")

plt.tight_layout()
plt.savefig("data/cba_analysis.png", dpi=150)
plt.show()