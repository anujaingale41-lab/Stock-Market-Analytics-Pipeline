def calculate_analytics(data):

    closes = [d.close for d in data]

    #returns
    returns = [(closes[i]-closes[i-1])/closes[i-1] for i in range(1,len(closes))]

    avg_return = sum(returns)/len(returns)
    total_return = ((closes[-1] - closes[0])/ closes[0]) *100

    #volatility
    mean = avg_return
    variance = sum((r - mean)**2 for r in returns) / len(returns)
    volatility=variance**0.5

    #max drawdown
    peak= closes[0]
    max_drawdown = 0

    for price in closes:
        if price> peak:
            peak= price
        drawdown = (peak-price)/peak
        if drawdown > max_drawdown:
           max_drawdown = drawdown

    #moving averages
    def moving_avg(data, window):
        return round(sum(data[-window:])/window, 2) if len(data) >= window else None
    
    ma_5 = moving_avg(closes, 5)
    ma_25 = moving_avg(closes, 25)

    return{
        'records': len(closes),
        'total_return_percent': round(total_return,2),
        'average_daily_return': round(avg_return,4),
        'volatitlity': round(volatility,4),
        'max_drawdown': round(max_drawdown,4),
        'moving_average_5': ma_5,
        'moving_average_25': ma_25
    }