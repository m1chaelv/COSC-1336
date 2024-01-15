prices=[3,13,1,3,6,4,12]

profit = 0
low = high = prices[0]
print('Start',low,high,'day',profit)

for day in prices:
    print('-',day,'-')
    if day < low:
        profit = max(profit, high - low)
        low = high = day
        print('Low',low,high,day,profit)
        continue

    if day > high:
        high = day
        print('High',low,high,day,profit)
        continue

prices.clear()
if (high - low) > profit:
    print(high - low)
else:
    print(profit)