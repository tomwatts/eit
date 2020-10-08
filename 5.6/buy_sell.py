# Returns max possible profit, 0 if profit not possible
def buy_sell(stock_prices):
    profit = 0

    for i in range(len(stock_prices) - 1):  # Stop before the final day
        buy_price = stock_prices[i]

        # Get the max price from the remaining days
        sell_price = 0
        for j in range(i+1, len(stock_prices)):
            if stock_prices[j] > sell_price:
                sell_price = stock_prices[j]

        possible_profit = sell_price - buy_price
        if possible_profit > profit:
            profit = possible_profit

    return profit


assert buy_sell([]) == 0
assert buy_sell([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30
assert buy_sell([310, 275, 260, 230]) == 0
assert buy_sell([295, 260, 270, 230]) == 10
