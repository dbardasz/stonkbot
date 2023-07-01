import yfinance as yf


def get_data(tkr):
    try:
        ticker = yf.Ticker(tkr)
        # get historical market data
        hist = ticker.history(period="30d")
        # get data
        previous_close = round(hist['Close'].iloc[-2], 2)
        todays_open = round(hist['Open'].iloc[-1], 2)
        month_high = round(hist['High'].max(), 2)
        # perform calculations
        percent_change = round((todays_open - previous_close) / previous_close, 4) * 100
        percent_string = str(percent_change) + '%'
        string = """{}: \nYesterday\'s Close: ${} \nToday\'s Open: ${} \nPercent Change: {} \nLast 30 Days High: ${}  
                    """.format(tkr, previous_close, todays_open, percent_string, month_high)
        return string
    except:
        return 'Check your ticker again dumbass'
