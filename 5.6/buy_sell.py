# Returns dict with buy and sell days as well as profit, none if profit not possible
def buy_sell(stock_prices):
    profit = 0
    for i in range(len(stock_prices) - 1):  # Stop on the final day
        buy_price = stock_prices[i]
        sell_price = max(stock_prices[i+1:])
        profit = max(profit, sell_price - buy_price)

    return profit


assert buy_sell([]) == 0
assert buy_sell([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30
assert buy_sell([310, 275, 260, 230]) == 0
assert buy_sell([295, 260, 270, 230]) == 10
