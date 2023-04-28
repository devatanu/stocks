import yfinance as yf
import matplotlib.pyplot as plt
import mpld3

# Define the ticker symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='50d')

# Calculate the moving averages
ma_9 = tickerDf['Close'].rolling(window=9).mean()
ma_20 = tickerDf['Close'].rolling(window=20).mean()

# Plot the closing prices and moving averages
fig, ax = plt.subplots()
ax.plot(tickerDf.index, tickerDf['Close'], label='Closing Price')
ax.plot(tickerDf.index, ma_9, label='9-day MA')
ax.plot(tickerDf.index, ma_20, label='20-day MA')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('Google Stock Price')
ax.legend()

# Convert the plot to HTML
html_fig = mpld3.fig_to_html(fig)

# Write the HTML to a file
with open('plot.html', 'w') as f:
    f.write(html_fig)