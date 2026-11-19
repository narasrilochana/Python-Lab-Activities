
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

df["Date"] = pd.to_datetime(df["Date"])

daily_sales = df.groupby(["Date", "Product"])["Sales"].sum().unstack()

daily_sales.plot(kind="line", marker="o")
plt.title("Daily Retail Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend(title="Product")
plt.grid(True)
plt.show()

product_sales = df.groupby("Product")["Sales"].sum()

product_sales.plot(kind="bar", color=["blue", "orange"])
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.show()
