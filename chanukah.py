def NumofCandles(s):
    candle = s[0]
    days = s[1]
    
    Candlesneeded = days + ((days * (days + 1))/2)
    print('{0} {1}'.format(candle, int(Candlesneeded)))
    
n = int(input())
for i in range(n):
    s = [int(j) for j in input().split()]
    NumofCandles(s)
