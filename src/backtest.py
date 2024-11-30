
def backtest_strategy(data, initial_capital, fee_percentage):
    data = data.copy()
    cash = initial_capital
    holdings = 0
    portfolio_values = []
    for i in range(len(data)):
        price = data['Close'].iloc[i]
        signal = data['Signal'].iloc[i]
        if signal == 1:  # Buy
            shares = cash // price
            cash -= shares * price
            holdings += shares
        elif signal == -1 and holdings > 0:  # Sell
            cash += holdings * price
            holdings = 0
        portfolio_values.append(cash + holdings * price)
    data['Portfolio Value'] = portfolio_values
    return data
