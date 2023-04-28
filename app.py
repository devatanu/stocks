@app.route("/")
def home():
    return render_template("home.html")

@app.route("/plot", methods=["GET", "POST"])
def plot():
    if request.method == "POST":
        tickerSymbol = request.form["ticker"]
        tickerData = yf.Ticker(tickerSymbol)
        tickerDf = tickerData.history(period="50d")
        tickerDf.index.name = "Date"
        tickerDf = tickerDf.reset_index()
        ma9 = pd.Series(tickerDf["Close"].rolling(window=9).mean(), name="MA9")
        ma20 = pd.Series(tickerDf["Close"].rolling(window=20).mean(), name="MA20")
        tickerDf = pd.concat([tickerDf, ma9, ma20], axis=1)
        tickerDf = tickerDf.set_index("Date")
        fig, ax = mpf.plot(tickerDf, type="candle", mav=(9, 20), volume=True, show_nontrading=True, returnfig=True)
        plt.title(f"{tickerSymbol.upper()} Stock Price")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.tight_layout()
        fig.savefig("static/plot.png")
        return render_template("plot.html", ticker=tickerSymbol.upper())
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)